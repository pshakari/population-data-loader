# winemap-data-loader
Creates a postgresql container on OpenShift and then loads wine review data from a data loader image as a kubernetes [job](http://kubernetesbyexample.com/jobs/)


```sh
oc cluster up

oc new-project population

oc new-app --template=postgresql-persistent \
-p POSTGRESQL_USER=username \
-p POSTGRESQL_PASSWORD=password \
-p POSTGRESQL_DATABASE=populationDb

```

```sh
oc create -f https://raw.githubusercontent.com/radanalyticsio/winemap-data-loader/master/wine-data-loader.yaml

oc new-app --template=population-data-loader
```
