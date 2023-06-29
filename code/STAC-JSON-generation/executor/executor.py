from github import Github
from builder import dictionary_builder
from builder import builder_interface
import config


# importing values from the configuration file
# authentication token
GH_TOKEN = config.GH_TOKEN
# repository name
repository = config.repository
# issue labels to download
labels = config.labels
# folders for saving data
markdown_folder = config.markdown_folder
stac_files_folder = config.stac_files_folder


# execution of the entire application:
# download of issues -> building of dictionaries -> building of STAC files -> publication on GitHub.
def run():
    github_connection = Github(GH_TOKEN)
    # download all issues with <label = "a/p resource metadata">
    issues = github_connection.get_repo(repository).get_issues(labels=labels)
    # iteration for each issue with label='a/p resource metadata'
    for i in range(issues.totalCount):
        page = issues.get_page(i)
        for j in range(len(page)):
            print('\n---> Executing issue ' + page[j].title + ' <---')
            title = page[j].title
            body = page[j].body

            # txt and STAC file generation
            txt_filename = markdown_folder + title + '.txt'
            stac_filename = stac_files_folder + title + '.json'

            # writing the txt file
            with open(txt_filename, 'w+') as f:
                f.write(body)
            f.close()

            # dictionary building
            dictionary = dictionary_builder.get_dictionary(txt_filename)
            # STAC file building
            collection_filename = builder_interface.build_stac_file(dictionary, stac_filename, title)

            # opening the file to be uploaded to GitHub
            with open(stac_filename, 'r') as stac:
                stac_file = stac.read()
            stac.close()

            # opening the collection to be updated to GitHub
            with open(collection_filename, 'r') as c:
                collection_file = c.read()
            c.close()

            # with open(txt_filename, 'r') as markdown:
            #     markdown_file = markdown.read()
            # markdown.close()

            # opening the GitHub repository
            repo = github_connection.get_repo(repository)

            # checking if files are in repository -> in this case must be update
            # markdown_in_repo = False
            stac_in_repo = False
            # sha_markdown = ''
            sha_stac = ''
            # sha collection
            sha_collection = ''
            files = repo.get_contents(config.stac_files_repo_folder)
            collection = ''
            for f in range(len(files)):
                if files[f].path == stac_filename:
                    stac_in_repo = True
                    sha_stac = files[f].sha
                if files[f].path == collection_filename:
                    sha_collection = files[f].sha
                # if files[f].path == txt_filename:
                #     markdown_in_repo = True
                #     sha_markdown = files[f].sha
                #     continue

            # publishing to GitHub
            # if markdown_in_repo:
            #     repo.update_file(txt_filename, 'update', markdown_file, sha_markdown, branch="master")
            # else:
            #     repo.create_file(txt_filename, 'upload', markdown_file, 'master')
            if stac_in_repo:
                repo.update_file(stac_filename, 'update', stac_file, sha_stac, branch="main")
            else:
                repo.create_file(stac_filename, 'upload', stac_file, branch='main')
            print('STAC file uploaded...')
            # collection updating
            repo.update_file(collection_filename, 'update', collection_file, sha_collection, branch='main')
            print('collection updated')
    print('\n\nExecution completed')
