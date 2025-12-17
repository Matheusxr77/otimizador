echo "Iniciando Cluster Geo-Distribuído..."
minikube start --nodes 4 -p geo-cluster --driver=docker

echo "Aplicando Labels..."
kubectl label node geo-cluster-m02 region=us-east --overwrite
kubectl label node geo-cluster-m03 region=eu-west --overwrite
kubectl label node geo-cluster-m04 region=asia-pacific --overwrite

echo "Ambiente Pronto!"