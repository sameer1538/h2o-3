library(h2o)
h2o.init()
path = system.file("extdata", "prostate.csv", package = "h2o")
h2o_df = h2o.importFile(path)
h2o_df$CAPSULE = as.factor(h2o_df$CAPSULE)
binomial.fit = h2o.glm(y = "CAPSULE", x = c("AGE", "RACE", "PSA", "GLEASON"), training_frame = h2o_df, family = "binomial", nfolds = 5)
print(binomial.fit)
print(paste("training auc:        ", binomial.fit@model$training_metrics@metrics$AUC))
print(paste("cross-validation auc:", binomial.fit@model$cross_validation_metrics@metrics$AUC))
