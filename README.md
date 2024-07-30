# Resource Metadata
The purpose of this repository is to govern the creation and maintenance of metadata of processing/analysis (a/p) resources. 
Aspects related to the governance of codelists apply also to datasets metadata. 

To create the metadata file for a new a/p resource as well as to update an existing one use the dedicated [web application](https://fairicube-md.dev.epsilon-italia.it/). 

The created metadata file will automatically be published in the [FAIRiCUBE Catalogue](https://catalog.eoxhub.fairicube.eu/?.language=en) and will be queryable through [Knowledge Base Query Tool](https://fairicube-kb.dev.epsilon-italia.it/query-tool).

To ensure semantic harmonisation, some metadata elements are valorised by selecting values from corresponding codelists. Use the [Codelist change proposal template](https://github.com/FAIRiCUBE/resource-metadata/issues/new?assignees=&labels=&projects=&template=codelist_change_proposal.yml) for proposing updates to current codelists. 


## Analysis and processing resources metadata codelists
NB: Each column corresponds to a codelist. The column header (in *italics*) is the codelist name.

| *Main category* | *Objective* | *Platform* | *Framework* | *Architecture* | *Approach* | *Algorithm* | *Processor* | *OS* | *Use case* | *Conditions for access and use* |
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|Machine Learning|object-detection|EOX|pytorch|random forest|supervised|Random-Forest-Classifier|cpu|aix|UC1|afl-3.0|
|Deep Learning|classification|Rasdaman|tensorflow|DNN – Deep-Neural-Network |unsupervised|CNN - Convolutional-Neural-Network|gpu|linux|UC2|agpl-3.0|
|Pre-processing|segmentation|Google Colab|scikit-learn|decision-tree|semi-supervised|K-means|tpu|windows|UC3|artistic-2.0|
|Ingestion|regression|Kaggle|keras|ensemble  |reinforcement-learning|Min-max-normalization| |cygwin|UC4|bigscience-bloom-rail-1.0|
|Analytics|outliers-removing|Microsoft Azure|pandas|gradient-based| |DBSCAN - Density-Based-Spatial-Clustering-of-Applications-with-Noise| |darwin|UC5|bigscience-openrail-m|
| |gap-filling|Amazon AWS|numpy|density-based| |Decision-Tree-Classifier| |macOS|common|bsd|
| |feature-selection|Local Jupyter Notebook|openCV|datacubes| |Random-Forest-Regression| | | |bsd-2-clause|
| |dimensionality-reduction| |XGBoost|RNN – Recurrent-Neural-Network| |SGD - classifier – Stochastic-Gradient-Descent| | | |bsd-3-clause|
| |feature-scaling| |theano|CNN – Convolutional-Neural-Network| |KNN – classifier – K-nearest-neighbors| | | |bsd-3-clause-clear|
| |dataset-balancing| |imblearn|Feed-Forward-Neural-Network| |SegNet| | | |bsl-1.0|
| |data-transformation| |pillow|DBN – Deep-Belief-Network| |LeNet| | | |cc|
| |analytics| |Rasdaman|DSN – Deep-Stacking-Network| |Decision-Tree-Regression| | | |cc0-1.0|
| |clustering| |MXNet|SVM – Support-Vector-Machine| |Voting-Classifier| | | |cc-by-2.0|
| |anomaly-detection| |Apache-Spark|probabilistic model| |AdaBoost-Classifier| | | |cc-by-2.5|
| | | |gdal|Perceptron| |AdaBoost-Regression| | | |cc-by-3.0|
| | | |no-framework|Multilayer-Perceptron| |SMOTE – Synthetic-Minority-Oversampling-TEchnique| | | |cc-by-4.0|
| | | | | | |custom-method| | | |cc-by-nc-2.0|
| | | | | | |WCPS| | | |cc-by-nc-3.0|
| | | | | | |Naïve-Bayes| | | |cc-by-nc-4.0|
| | | | | | |Logistic-regression| | | |cc-by-nc-nd-3.0|
| | | | | | |Gaussian-Mixture| | | |cc-by-nc-nd-4.0|
| | | | | | | | | | |cc-by-nc-sa-2.0|
| | | | | | | | | | |cc-by-nc-sa-3.0|
| | | | | | | | | | |cc-by-nc-sa-4.0|
| | | | | | | | | | |cc-by-nd-4.0|
| | | | | | | | | | |cc-by-sa-3.0|
| | | | | | | | | | |cc-by-sa-4.0|
| | | | | | | | | | |creativeml-openrail-m|
| | | | | | | | | | |c-uda|
| | | | | | | | | | |ecl-2.0|
| | | | | | | | | | |epl-1.0|
| | | | | | | | | | |epl-2.0|
| | | | | | | | | | |eupl-1.1|
| | | | | | | | | | |gfdl|
| | | | | | | | | | |gpl|
| | | | | | | | | | |gpl-2.0|
| | | | | | | | | | |gpl-3.0|
| | | | | | | | | | |isc|
| | | | | | | | | | |lgpl|
| | | | | | | | | | |lgpl-2.1|
| | | | | | | | | | |lgpl-3.0|
| | | | | | | | | | |lgpl-lr|
| | | | | | | | | | |mpl-2.0|
| | | | | | | | | | |ms-pl|
| | | | | | | | | | |ncsa|
| | | | | | | | | | |odbl|
| | | | | | | | | | |odc-by|
| | | | | | | | | | |ofl-1.1|
| | | | | | | | | | |openrail|
| | | | | | | | | | |openrail++|
| | | | | | | | | | |osl-3.0|
| | | | | | | | | | |pddl|
| | | | | | | | | | |postgresql|
| | | | | | | | | | |wtfpl|


## Dataset metadata codelists
NB: Each column corresponds to a codelist. The column header (in *italics*) is the codelist name. For each codelist there are three fields on three different lines: the value, the definition and the link to a source providing more information.


|| *ObservableProperties* |
|---|---|
| *Value* | Water and Wetness |
| *Definition* | The HRL Water and Wetness 2018 provides primary products in full spatial resolution of 10m x 10m (as compared to 20m x 20m resolution in 2015). The main product is a classified layer, differentiating the classes of permanent water, temporary water, permanent wet, temporary wet, and dry areas, derived from water and wetness occurrences in the period 2012-2018. |
| *Source Link* | [Water and Wetness source link](https://land.copernicus.eu/en/technical-library/hrl-water-wetness-2018-user-manual/@@download/file) |
