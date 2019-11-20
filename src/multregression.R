url <- "https://raw.githubusercontent.com/sdbuit/callforecast/master/data/interim/02training.csv"
df <- read.table(url, sep = ",", header = T)[,-1]

#set.seed(1)
train = sample(1:nrow(df), floor(.7*nrow(df)), replace=FALSE)
lm <- lm(CV ~ as.factor(time24) + as.factor(day), data=df, subset=train)

error <- rep(NA, 500)    
for (i in c(1:500)) {
    train = sample(1:nrow(df), floor(.7*nrow(df)), replace=FALSE)
    test <- df[-train, "CV"]
    yhat <- predict(lm, newdata = df[-train,])
    error[i] <- mean((yhat - test)^2)
    #plot(yhat,test)
}
cat('Model (test 1) MSE:\t', round(mean(error), 2))

error <- rep(NA, 500)    
for (i in c(1:500)) {
    n = nrow(df)
    train <- sample(1:n, 1300)
    error[i] <- mean(((df$CV-predict(lm,df))[-train])^2)
}
cat('\nModel (test 2) MSE:\t', round(mean(error), 2))

# library(boot)
# glm.fit <- glm(CV ~ as.factor(time24) + as.factor(day), data=df)
# cv.err<-cv.glm(df,glm.fit)
# #cv.err$delta # LOOCV estimate test error approximately 3070.853
# 
# cv.error<-rep(0,5)
# for (i in 1:5){
#   cv.error[i]=cv.glm(df,glm.fit)$delta[1]
# }
# cv.error