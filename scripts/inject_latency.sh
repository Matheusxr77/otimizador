echo "Injetando Latência (Network Shaping)..."
minikube ssh -n geo-cluster-m02 -- sudo tc qdisc replace dev eth0 root netem delay 20ms
minikube ssh -n geo-cluster-m03 -- sudo tc qdisc replace dev eth0 root netem delay 150ms
minikube ssh -n geo-cluster-m04 -- sudo tc qdisc replace dev eth0 root netem delay 300ms
echo "Latência Configurada!"