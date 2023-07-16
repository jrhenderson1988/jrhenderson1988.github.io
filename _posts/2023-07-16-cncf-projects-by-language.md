---
title: CNCF Projects by Language
summary: "The projects within the CNCF Landscape listed by their primary programming language"
---
<style>
ul {
    list-style-type: circle;
}
</style>

Ever wanted to see a list of CNCF (Cloud-Native Computing Foundation) projects, grouped by their 
primary programming language? No? Just me?

Well, here's the list anyway. The projects are also grouped by their category, ordered by stars and
the languages are ordered by number of projects.

The data comes from the
[CNCF Landscape GitHub](https://github.com/cncf/landscape/blob/master/processed_landscape.yml) and
was massaged into a blog post using
[this Python script](
https://github.com/jrhenderson1988/jrhenderson1988.github.io/tree/master/scripts/cncf.py).



## <span style="color:#00ADD8;">&#9679;</span> Go <small>(308 projects)</small>

### Provisioning / Automation & Configuration
- Terraform <small> (&#9733; 36,977 / [Repository](https://github.com/hashicorp/terraform) / [Homepage](https://www.terraform.io/))</small>
- Pulumi <small> (&#9733; 15,726 / [Repository](https://github.com/pulumi/pulumi) / [Homepage](https://www.pulumi.com/))</small>
- LinuxKit <small> (&#9733; 7,777 / [Repository](https://github.com/linuxkit/linuxkit) / [Homepage](https://github.com/linuxkit/linuxkit))</small>
- Cadence Workflow <small> (&#9733; 6,771 / [Repository](https://github.com/uber/cadence) / [Homepage](https://cadenceworkflow.io/))</small>
- KubeEdge <small> (&#9733; 5,774 / [Repository](https://github.com/kubeedge/kubeedge) / [Homepage](https://kubeedge.io/en/))</small>
- Juju <small> (&#9733; 2,120 / [Repository](https://github.com/juju/juju) / [Homepage](https://jaas.ai/))</small>
- OpenYurt <small> (&#9733; 1,443 / [Repository](https://github.com/openyurtio/openyurt) / [Homepage](https://openyurt.io/))</small>
- kiosk <small> (&#9733; 975 / [Repository](https://github.com/loft-sh/kiosk) / [Homepage](https://github.com/loft-sh/kiosk))</small>
- SuperEdge <small> (&#9733; 919 / [Repository](https://github.com/superedge/superedge) / [Homepage](https://superedge.io/))</small>
- Shifu <small> (&#9733; 853 / [Repository](https://github.com/edgenesis/shifu) / [Homepage](https://shifu.dev/))</small>
- Tinkerbell <small> (&#9733; 751 / [Repository](https://github.com/tinkerbell/tink) / [Homepage](https://tinkerbell.org/))</small>
- DevStream <small> (&#9733; 747 / [Repository](https://github.com/devstream-io/devstream) / [Homepage](https://www.devstream.io/))</small>
- KubeZoo <small> (&#9733; 551 / [Repository](https://github.com/kubewharf/kubezoo) / [Homepage](https://kubewharf.github.io))</small>
- KusionStack <small> (&#9733; 512 / [Repository](https://github.com/KusionStack/kusion) / [Homepage](https://kusionstack.io/))</small>
- Kubefirst <small> (&#9733; 498 / [Repository](https://github.com/kubefirst/kubefirst) / [Homepage](https://docs.kubefirst.com))</small>
- KubeDL <small> (&#9733; 424 / [Repository](https://github.com/kubedl-io/kubedl) / [Homepage](https://kubedl.io))</small>
- Metal³ <small> (&#9733; 420 / [Repository](https://github.com/metal3-io/baremetal-operator) / [Homepage](https://metal3.io/))</small>
- Digital Rebar <small> (&#9733; 136 / [Repository](https://github.com/digitalrebar/provision) / [Homepage](https://rackn.com/rebar/))</small>

### Provisioning / Container Registry
- Harbor <small> (&#9733; 19,867 / [Repository](https://github.com/goharbor/harbor) / [Homepage](https://goharbor.io/))</small>
- Distribution <small> (&#9733; 7,447 / [Repository](https://github.com/distribution/distribution) / [Homepage](https://github.com/distribution/distribution))</small>
- Kraken <small> (&#9733; 5,418 / [Repository](https://github.com/uber/kraken) / [Homepage](https://eng.uber.com/introducing-kraken/))</small>
- Dragonfly <small> (&#9733; 1,289 / [Repository](https://github.com/dragonflyoss/Dragonfly2) / [Homepage](https://d7y.io/))</small>
- zot <small> (&#9733; 344 / [Repository](https://github.com/project-zot/zot) / [Homepage](https://zotregistry.io/))</small>

### Provisioning / Security & Compliance
- Trivy <small> (&#9733; 17,042 / [Repository](https://github.com/aquasecurity/trivy) / [Homepage](https://github.com/aquasecurity/trivy))</small>
- SlimToolkit <small> (&#9733; 16,749 / [Repository](https://github.com/slimtoolkit/slim) / [Homepage](https://slimtoolkit.org/))</small>
- cert-manager <small> (&#9733; 10,219 / [Repository](https://github.com/cert-manager/cert-manager) / [Homepage](https://cert-manager.io/))</small>
- Clair <small> (&#9733; 9,464 / [Repository](https://github.com/quay/clair) / [Homepage](https://www.redhat.com/en/topics/containers/what-is-clair))</small>
- Kubescape <small> (&#9733; 8,293 / [Repository](https://github.com/kubescape/kubescape) / [Homepage](https://kubescape.io/))</small>
- Dex <small> (&#9733; 8,031 / [Repository](https://github.com/dexidp/dex) / [Homepage](https://dexidp.io/))</small>
- Open Policy Agent (OPA) <small> (&#9733; 7,935 / [Repository](https://github.com/open-policy-agent/opa) / [Homepage](https://www.openpolicyagent.org/))</small>
- Datree <small> (&#9733; 6,230 / [Repository](https://github.com/datreeio/datree) / [Homepage](https://datree.io/))</small>
- kube-bench <small> (&#9733; 5,773 / [Repository](https://github.com/aquasecurity/kube-bench) / [Homepage](https://github.com/aquasecurity/kube-bench))</small>
- Terrascan <small> (&#9733; 4,001 / [Repository](https://github.com/tenable/terrascan) / [Homepage](https://www.tenable.com/products/tenable-cs))</small>
- Kyverno <small> (&#9733; 3,778 / [Repository](https://github.com/kyverno/kyverno) / [Homepage](https://kyverno.io/))</small>
- ThreatMapper <small> (&#9733; 3,664 / [Repository](https://github.com/deepfence/ThreatMapper) / [Homepage](https://deepfence.io/threatmapper/))</small>
- Notary <small> (&#9733; 3,013 / [Repository](https://github.com/notaryproject/notary) / [Homepage](https://notaryproject.dev/))</small>
- Polaris <small> (&#9733; 2,857 / [Repository](https://github.com/FairwindsOps/polaris) / [Homepage](https://fairwinds.com/polaris))</small>
- Sonobuoy <small> (&#9733; 2,719 / [Repository](https://github.com/vmware-tanzu/sonobuoy) / [Homepage](https://sonobuoy.io))</small>
- external-secrets <small> (&#9733; 2,551 / [Repository](https://github.com/external-secrets/external-secrets) / [Homepage](https://external-secrets.io/))</small>
- ContainerSSH <small> (&#9733; 2,282 / [Repository](https://github.com/containerssh/containerssh) / [Homepage](https://containerssh.io))</small>
- Goldilocks <small> (&#9733; 1,802 / [Repository](https://github.com/FairwindsOps/goldilocks) / [Homepage](https://www.fairwinds.com/open-source-software))</small>
- Pluto <small> (&#9733; 1,500 / [Repository](https://github.com/FairwindsOps/pluto) / [Homepage](https://www.fairwinds.com/open-source-software))</small>
- Grafeas <small> (&#9733; 1,436 / [Repository](https://github.com/grafeas/grafeas) / [Homepage](https://grafeas.io/))</small>
- Cerbos <small> (&#9733; 1,299 / [Repository](https://github.com/cerbos/cerbos) / [Homepage](https://www.cerbos.dev/))</small>
- RBAC Manager <small> (&#9733; 1,227 / [Repository](https://github.com/FairwindsOps/rbac-manager) / [Homepage](https://www.fairwinds.com/open-source-software))</small>
- Veinmind Tools <small> (&#9733; 1,217 / [Repository](https://github.com/chaitin/veinmind-tools) / [Homepage](https://veinmind.chaitin.com/))</small>
- KubeClarity <small> (&#9733; 970 / [Repository](https://github.com/openclarity/kubeclarity) / [Homepage](https://openclarity.io/))</small>
- OpenFGA <small> (&#9733; 903 / [Repository](https://github.com/openfga/openfga) / [Homepage](https://openfga.dev))</small>
- NeuVector <small> (&#9733; 744 / [Repository](https://github.com/neuvector/neuvector) / [Homepage](https://neuvector.com/))</small>
- Paralus <small> (&#9733; 740 / [Repository](https://github.com/paralus/paralus) / [Homepage](https://www.paralus.io/))</small>
- RBAC Lookup <small> (&#9733; 730 / [Repository](https://github.com/FairwindsOps/rbac-lookup) / [Homepage](https://www.fairwinds.com/open-source-software))</small>
- KubeArmor <small> (&#9733; 680 / [Repository](https://github.com/kubearmor/kubearmor) / [Homepage](https://kubearmor.io/))</small>
- Topaz <small> (&#9733; 639 / [Repository](https://github.com/aserto-dev/topaz) / [Homepage](https://www.topaz.sh))</small>
- Trivy-Operator <small> (&#9733; 498 / [Repository](https://github.com/aquasecurity/trivy-operator) / [Homepage](https://github.com/aquasecurity/trivy-operator))</small>
- APIClarity <small> (&#9733; 398 / [Repository](https://github.com/openclarity/apiclarity) / [Homepage](https://openclarity.io/))</small>
- sigstore <small> (&#9733; 363 / [Repository](https://github.com/sigstore/sigstore) / [Homepage](https://www.sigstore.dev/))</small>
- Open Policy Containers <small> (&#9733; 152 / [Repository](https://github.com/opcr-io/policy) / [Homepage](https://openpolicycontainers.com))</small>
- Kubewarden <small> (&#9733; 118 / [Repository](https://github.com/kubewarden/kubewarden-controller) / [Homepage](https://www.kubewarden.io))</small>
- Hexa <small> (&#9733; 63 / [Repository](https://github.com/hexa-org/policy-orchestrator) / [Homepage](https://hexaorchestration.org/))</small>
- VMClarity <small> (&#9733; 40 / [Repository](https://github.com/openclarity/vmclarity) / [Homepage](https://openclarity.io/))</small>
- Aserto <small> (&#9733; 23 / [Repository](https://github.com/aserto-dev/runtime) / [Homepage](https://www.aserto.com))</small>

### Provisioning / Key Management
- Vault <small> (&#9733; 27,546 / [Repository](https://github.com/hashicorp/vault) / [Homepage](https://www.vaultproject.io/))</small>
- Teleport <small> (&#9733; 14,225 / [Repository](https://github.com/gravitational/teleport) / [Homepage](https://goteleport.com))</small>
- ORY Hydra <small> (&#9733; 13,956 / [Repository](https://github.com/ory/hydra) / [Homepage](https://www.ory.sh/))</small>
- OAuth2 Proxy <small> (&#9733; 6,839 / [Repository](https://github.com/oauth2-proxy/oauth2-proxy) / [Homepage](https://oauth2-proxy.github.io/oauth2-proxy/))</small>
- Pomerium <small> (&#9733; 3,504 / [Repository](https://github.com/pomerium/pomerium) / [Homepage](https://www.pomerium.com))</small>
- sso <small> (&#9733; 3,005 / [Repository](https://github.com/buzzfeed/sso) / [Homepage](https://github.com/buzzfeed/sso))</small>
- Teller <small> (&#9733; 1,636 / [Repository](https://github.com/tellerops/teller) / [Homepage](https://tlr.dev))</small>
- SPIRE <small> (&#9733; 1,392 / [Repository](https://github.com/spiffe/spire) / [Homepage](https://spiffe.io/spire/))</small>
- Pinniped <small> (&#9733; 411 / [Repository](https://github.com/vmware-tanzu/pinniped) / [Homepage](https://pinniped.dev))</small>

### Runtime / Cloud Native Storage
- MinIO <small> (&#9733; 38,591 / [Repository](https://github.com/minio/minio) / [Homepage](https://min.io/))</small>
- JuiceFS <small> (&#9733; 7,875 / [Repository](https://github.com/juicedata/juicefs) / [Homepage](https://juicefs.com/))</small>
- Velero <small> (&#9733; 7,241 / [Repository](https://github.com/vmware-tanzu/velero) / [Homepage](https://velero.io))</small>
- Stash by AppsCode <small> (&#9733; 1,186 / [Repository](https://github.com/stashed/stash) / [Homepage](https://stash.run))</small>
- ORAS <small> (&#9733; 908 / [Repository](https://github.com/oras-project/oras) / [Homepage](https://oras.land/))</small>
- Soda Foundation <small> (&#9733; 821 / [Repository](https://github.com/sodafoundation/api) / [Homepage](https://sodafoundation.io/wp-content/uploads/2021/03/cn.png))</small>
- Carina <small> (&#9733; 605 / [Repository](https://github.com/carina-io/carina) / [Homepage](http://www.opencarina.com))</small>
- K8up <small> (&#9733; 404 / [Repository](https://github.com/k8up-io/k8up) / [Homepage](https://www.k8up.io/))</small>
- HwameiStor <small> (&#9733; 376 / [Repository](https://github.com/hwameistor/hwameistor) / [Homepage](https://hwameistor.io/))</small>

### Runtime / Container Runtime
- containerd <small> (&#9733; 13,753 / [Repository](https://github.com/containerd/containerd) / [Homepage](https://containerd.io/))</small>
- gVisor <small> (&#9733; 13,716 / [Repository](https://github.com/google/gvisor) / [Homepage](https://gvisor.dev/))</small>
- Lima <small> (&#9733; 11,299 / [Repository](https://github.com/lima-vm/lima) / [Homepage](https://github.com/lima-vm/lima))</small>
- runc <small> (&#9733; 10,257 / [Repository](https://github.com/opencontainers/runc) / [Homepage](https://www.opencontainers.org/))</small>
- rkt <small> (&#9733; 8,850 / [Repository](https://github.com/rkt/rkt) / [Homepage](https://github.com/rkt/rkt))</small>
- CRI-O <small> (&#9733; 4,511 / [Repository](https://github.com/cri-o/cri-o) / [Homepage](https://cri-o.io/))</small>
- lxd <small> (&#9733; 3,790 / [Repository](https://github.com/lxc/lxd) / [Homepage](https://linuxcontainers.org/lxd/))</small>
- Singularity <small> (&#9733; 2,425 / [Repository](https://github.com/apptainer/singularity) / [Homepage](https://sylabs.io/))</small>
- Kata Containers <small> (&#9733; 2,119 / [Repository](https://github.com/kata-containers/runtime) / [Homepage](https://katacontainers.io/))</small>

### Runtime / Cloud Native Network
- Cilium <small> (&#9733; 15,080 / [Repository](https://github.com/cilium/cilium) / [Homepage](https://cilium.io/))</small>
- Flannel <small> (&#9733; 7,925 / [Repository](https://github.com/flannel-io/flannel) / [Homepage](https://github.com/flannel-io/flannel))</small>
- Weave Net <small> (&#9733; 6,457 / [Repository](https://github.com/weaveworks/weave) / [Homepage](https://www.weave.works/oss/net/))</small>
- Container Network Interface (CNI) <small> (&#9733; 4,805 / [Repository](https://github.com/containernetworking/cni) / [Homepage](https://www.cni.dev/))</small>
- Project Calico <small> (&#9733; 4,537 / [Repository](https://github.com/projectcalico/calico) / [Homepage](https://www.tigera.io/project-calico))</small>
- Submariner <small> (&#9733; 2,105 / [Repository](https://github.com/submariner-io/submariner) / [Homepage](https://submariner.io))</small>
- Kube-router <small> (&#9733; 2,049 / [Repository](https://github.com/cloudnativelabs/kube-router) / [Homepage](https://www.kube-router.io))</small>
- Multus <small> (&#9733; 1,796 / [Repository](https://github.com/k8snetworkplumbingwg/multus-cni) / [Homepage](https://networkbuilders.intel.com/intel-technologies/container-experience-kits))</small>
- Kilo <small> (&#9733; 1,739 / [Repository](https://github.com/squat/kilo) / [Homepage](https://kilo.squat.ai))</small>
- Kube-OVN <small> (&#9733; 1,546 / [Repository](https://github.com/kubeovn/kube-ovn) / [Homepage](https://kubeovn.github.io/docs/en/))</small>
- Antrea <small> (&#9733; 1,447 / [Repository](https://github.com/antrea-io/antrea) / [Homepage](https://antrea.io/))</small>
- Network Service Mesh <small> (&#9733; 507 / [Repository](https://github.com/networkservicemesh/networkservicemesh) / [Homepage](https://networkservicemesh.io/))</small>
- CNI-Genie <small> (&#9733; 500 / [Repository](https://github.com/cni-genie/CNI-Genie) / [Homepage](https://cnigenie.netlify.app))</small>
- FabEdge <small> (&#9733; 478 / [Repository](https://github.com/FabEdge/fabedge) / [Homepage](https://www.fabedge.io/))</small>
- DANM <small> (&#9733; 347 / [Repository](https://github.com/nokia/danm) / [Homepage](https://github.com/nokia/danm))</small>
- Spiderpool <small> (&#9733; 319 / [Repository](https://github.com/spidernet-io/spiderpool) / [Homepage](https://spidernet-io.github.io/spiderpool/))</small>
- Ligato <small> (&#9733; 215 / [Repository](https://github.com/ligato/vpp-agent) / [Homepage](https://ligato.io/))</small>

### Orchestration & Management / Scheduling & Orchestration
- Kubernetes <small> (&#9733; 97,680 / [Repository](https://github.com/kubernetes/kubernetes) / [Homepage](https://kubernetes.io/))</small>
- Nomad <small> (&#9733; 13,489 / [Repository](https://github.com/hashicorp/nomad) / [Homepage](https://www.nomadproject.io/))</small>
- Crossplane <small> (&#9733; 6,897 / [Repository](https://github.com/crossplane/crossplane) / [Homepage](https://crossplane.io/))</small>
- Karmada <small> (&#9733; 3,213 / [Repository](https://github.com/karmada-io/karmada) / [Homepage](https://karmada.io/))</small>
- Docker Swarm <small> (&#9733; 2,998 / [Repository](https://github.com/moby/swarmkit) / [Homepage](https://docs.docker.com/engine/swarm/))</small>
- Volcano <small> (&#9733; 2,947 / [Repository](https://github.com/volcano-sh/volcano) / [Homepage](https://volcano.sh/))</small>
- Kured <small> (&#9733; 1,786 / [Repository](https://github.com/kubereboot/kured) / [Homepage](https://kured.dev))</small>
- Fluid <small> (&#9733; 1,288 / [Repository](https://github.com/fluid-cloudnative/fluid) / [Homepage](http://pasa-bigdata.nju.edu.cn/fluid/index.html))</small>
- Capsule <small> (&#9733; 1,140 / [Repository](https://github.com/clastix/capsule) / [Homepage](https://capsule.clastix.io))</small>
- Clusternet <small> (&#9733; 1,140 / [Repository](https://github.com/clusternet/clusternet) / [Homepage](https://clusternet.io))</small>
- Koordinator <small> (&#9733; 824 / [Repository](https://github.com/koordinator-sh/koordinator) / [Homepage](https://koordinator.sh))</small>
- Clusterpedia <small> (&#9733; 577 / [Repository](https://github.com/clusterpedia-io/clusterpedia) / [Homepage](https://clusterpedia.io))</small>
- kube-green <small> (&#9733; 477 / [Repository](https://github.com/kube-green/kube-green) / [Homepage](https://kube-green.dev/))</small>
- Armada <small> (&#9733; 295 / [Repository](https://github.com/armadaproject/armada) / [Homepage](https://armadaproject.io/))</small>

### Orchestration & Management / Coordination & Service Discovery
- etcd <small> (&#9733; 43,211 / [Repository](https://github.com/etcd-io/etcd) / [Homepage](https://etcd.io/))</small>
- CoreDNS <small> (&#9733; 10,545 / [Repository](https://github.com/coredns/coredns) / [Homepage](https://coredns.io/))</small>
- KubeBrain <small> (&#9733; 585 / [Repository](https://github.com/kubewharf/kubebrain) / [Homepage](https://github.com/kubewharf/kubebrain))</small>
- k8gb <small> (&#9733; 563 / [Repository](https://github.com/k8gb-io/k8gb) / [Homepage](https://www.k8gb.io))</small>

### Orchestration & Management / Remote Procedure Call
- go-zero <small> (&#9733; 23,842 / [Repository](https://github.com/zeromicro/go-zero) / [Homepage](https://go-zero.dev/))</small>
- kratos <small> (&#9733; 20,458 / [Repository](https://github.com/go-kratos/kratos) / [Homepage](https://go-kratos.dev/))</small>
- CloudWeGo <small> (&#9733; 5,822 / [Repository](https://github.com/cloudwego/kitex) / [Homepage](https://www.cloudwego.io/))</small>

### Orchestration & Management / Service Proxy
- Caddy <small> (&#9733; 46,872 / [Repository](https://github.com/caddyserver/caddy) / [Homepage](https://caddyserver.com/))</small>
- Traefik <small> (&#9733; 42,640 / [Repository](https://github.com/traefik/traefik) / [Homepage](https://traefik.io/traefik))</small>
- BFE <small> (&#9733; 5,831 / [Repository](https://github.com/bfenetworks/bfe) / [Homepage](https://www.bfe-networks.net))</small>
- MetalLB <small> (&#9733; 5,727 / [Repository](https://github.com/metallb/metallb) / [Homepage](https://metallb.universe.tf))</small>
- MOSN <small> (&#9733; 4,120 / [Repository](https://github.com/mosn/mosn) / [Homepage](https://mosn.io))</small>
- Contour <small> (&#9733; 3,385 / [Repository](https://github.com/projectcontour/contour) / [Homepage](https://projectcontour.io))</small>
- Skipper <small> (&#9733; 2,852 / [Repository](https://github.com/zalando/skipper) / [Homepage](https://opensource.zalando.com/skipper/))</small>
- OpenELB <small> (&#9733; 1,308 / [Repository](https://github.com/openelb/openelb) / [Homepage](https://openelb.github.io))</small>
- STUNner <small> (&#9733; 481 / [Repository](https://github.com/l7mp/stunner) / [Homepage](https://l7mp.io))</small>

### Orchestration & Management / API Gateway
- Tyk <small> (&#9733; 8,327 / [Repository](https://github.com/TykTechnologies/tyk) / [Homepage](https://tyk.io/))</small>
- KrakenD <small> (&#9733; 5,509 / [Repository](https://github.com/luraproject/lura) / [Homepage](https://www.krakend.io/))</small>
- Easegress <small> (&#9733; 5,128 / [Repository](https://github.com/megaease/easegress) / [Homepage](https://megaease.com/easegress))</small>
- Gloo <small> (&#9733; 3,761 / [Repository](https://github.com/solo-io/gloo) / [Homepage](https://www.solo.io))</small>
- KubeGateway <small> (&#9733; 358 / [Repository](https://github.com/kubewharf/kubegateway) / [Homepage](https://github.com/kubewharf/kubegateway))</small>
- Kusk Gateway <small> (&#9733; 200 / [Repository](https://github.com/kubeshop/kusk-gateway) / [Homepage](https://kusk.kubeshop.io/))</small>
- EnRoute OneStep Ingress <small> (&#9733; 179 / [Repository](https://github.com/saarasio/enroute) / [Homepage](https://www.getenroute.io))</small>

### Orchestration & Management / Service Mesh
- Istio <small> (&#9733; 32,828 / [Repository](https://github.com/istio/istio) / [Homepage](https://istio.io/))</small>
- Consul <small> (&#9733; 26,314 / [Repository](https://github.com/hashicorp/consul) / [Homepage](https://www.consul.io/))</small>
- Linkerd <small> (&#9733; 9,519 / [Repository](https://github.com/linkerd/linkerd2) / [Homepage](https://linkerd.io/))</small>
- Kuma <small> (&#9733; 3,127 / [Repository](https://github.com/kumahq/kuma) / [Homepage](https://kuma.io))</small>
- Open Service Mesh <small> (&#9733; 2,567 / [Repository](https://github.com/openservicemesh/osm) / [Homepage](https://openservicemesh.io/))</small>
- Meshery <small> (&#9733; 2,031 / [Repository](https://github.com/meshery/meshery) / [Homepage](https://meshery.io))</small>
- Traefik Mesh <small> (&#9733; 1,853 / [Repository](https://github.com/traefik/mesh) / [Homepage](https://traefik.io/traefik-mesh))</small>
- Gloo Mesh <small> (&#9733; 1,015 / [Repository](https://github.com/solo-io/gloo-mesh) / [Homepage](https://docs.solo.io/gloo-mesh-enterprise/latest))</small>
- Aeraki Mesh <small> (&#9733; 650 / [Repository](https://github.com/aeraki-mesh/aeraki) / [Homepage](https://www.aeraki.net/))</small>
- Merbridge <small> (&#9733; 587 / [Repository](https://github.com/merbridge/merbridge) / [Homepage](https://merbridge.io/))</small>
- EaseMesh <small> (&#9733; 461 / [Repository](https://github.com/megaease/easemesh) / [Homepage](https://megaease.com/easemesh))</small>
- Slime <small> (&#9733; 373 / [Repository](https://github.com/slime-io/slime) / [Homepage](https://github.com/slime-io))</small>
- Nasp <small> (&#9733; 34 / [Repository](https://github.com/cisco-open/nasp) / [Homepage](https://github.com/cisco-open/nasp))</small>
- Flomesh Service Mesh (FSM) <small> (&#9733; 5 / [Repository](https://github.com/flomesh-io/fsm) / [Homepage](https://flomesh.io/))</small>

### App Definition and Development / Database
- TiDB <small> (&#9733; 33,910 / [Repository](https://github.com/pingcap/tidb) / [Homepage](https://en.pingcap.com))</small>
- CockroachDB <small> (&#9733; 26,980 / [Repository](https://github.com/cockroachdb/cockroach) / [Homepage](https://www.cockroachlabs.com/))</small>
- Dgraph <small> (&#9733; 19,190 / [Repository](https://github.com/dgraph-io/dgraph) / [Homepage](https://dgraph.io/))</small>
- Vitess <small> (&#9733; 16,067 / [Repository](https://github.com/vitessio/vitess) / [Homepage](https://vitess.io/))</small>
- NomsDB <small> (&#9733; 7,466 / [Repository](https://github.com/attic-labs/noms) / [Homepage](https://github.com/attic-labs/noms))</small>
- Weaviate <small> (&#9733; 5,183 / [Repository](https://github.com/semi-technologies/weaviate) / [Homepage](https://weaviate.io/developers/weaviate/current/index.html))</small>
- Stolon <small> (&#9733; 4,157 / [Repository](https://github.com/sorintlab/stolon) / [Homepage](https://sorintoss.io/projects/))</small>
- SpiceDB <small> (&#9733; 3,388 / [Repository](https://github.com/authzed/spicedb) / [Homepage](https://authzed.com/spicedb))</small>
- Crunchy Postgres Operator <small> (&#9733; 3,239 / [Repository](https://github.com/CrunchyData/postgres-operator) / [Homepage](https://www.crunchydata.com))</small>
- Pilosa <small> (&#9733; 2,444 / [Repository](https://github.com/pilosa/pilosa) / [Homepage](https://www.pilosa.com/))</small>
- SchemaHero <small> (&#9733; 767 / [Repository](https://github.com/schemahero/schemahero) / [Homepage](https://schemahero.io))</small>

### App Definition and Development / Streaming & Messaging
- NATS <small> (&#9733; 22,723 / [Repository](https://github.com/nats-io/nats-server) / [Homepage](https://nats.io/))</small>
- CloudEvents <small> (&#9733; 6,011 / [Repository](https://github.com/cloudevents/spec) / [Homepage](https://cloudevents.io/))</small>
- Pachyderm <small> (&#9733; 5,897 / [Repository](https://github.com/pachyderm/pachyderm) / [Homepage](https://www.pachyderm.com))</small>
- Memphis <small> (&#9733; 2,494 / [Repository](https://github.com/memphisdev/memphis-broker) / [Homepage](https://memphis.dev))</small>
- Koperator <small> (&#9733; 706 / [Repository](https://github.com/banzaicloud/koperator) / [Homepage](https://github.com/banzaicloud/koperator))</small>
- KubeMQ <small> (&#9733; 596 / [Repository](https://github.com/kubemq-io/kubemq-community) / [Homepage](https://kubemq.io/))</small>

### App Definition and Development / Application Definition & Image Build
- Docker Compose <small> (&#9733; 29,234 / [Repository](https://github.com/docker/compose) / [Homepage](https://docs.docker.com/compose/))</small>
- Helm <small> (&#9733; 24,171 / [Repository](https://github.com/helm/helm) / [Homepage](https://helm.sh/))</small>
- Podman <small> (&#9733; 17,628 / [Repository](https://github.com/containers/podman) / [Homepage](https://podman.io/))</small>
- Packer <small> (&#9733; 14,377 / [Repository](https://github.com/hashicorp/packer) / [Homepage](https://www.packer.io/))</small>
- Skaffold <small> (&#9733; 13,887 / [Repository](https://github.com/GoogleContainerTools/skaffold) / [Homepage](https://github.com/GoogleContainerTools/skaffold))</small>
- kaniko <small> (&#9733; 12,202 / [Repository](https://github.com/GoogleContainerTools/kaniko) / [Homepage](https://github.com/GoogleContainerTools/kaniko))</small>
- Tilt <small> (&#9733; 6,522 / [Repository](https://github.com/tilt-dev/tilt) / [Homepage](https://tilt.dev/))</small>
- Operator Framework <small> (&#9733; 6,455 / [Repository](https://github.com/operator-framework/operator-sdk) / [Homepage](https://www.redhat.com/en/technologies/cloud-computing/openshift/what-are-openshift-operators))</small>
- ko <small> (&#9733; 5,909 / [Repository](https://github.com/ko-build/ko) / [Homepage](https://ko.build/))</small>
- Telepresence <small> (&#9733; 5,752 / [Repository](https://github.com/telepresenceio/telepresence) / [Homepage](https://www.telepresence.io/))</small>
- KubeVela <small> (&#9733; 5,107 / [Repository](https://github.com/kubevela/kubevela) / [Homepage](https://kubevela.io))</small>
- KubeVirt <small> (&#9733; 4,042 / [Repository](https://github.com/kubevirt/kubevirt) / [Homepage](https://kubevirt.io/))</small>
- DevSpace <small> (&#9733; 3,475 / [Repository](https://github.com/devspace-sh/devspace) / [Homepage](https://devspace.sh))</small>
- Okteto <small> (&#9733; 2,872 / [Repository](https://github.com/okteto/okteto) / [Homepage](https://okteto.com/))</small>
- Buildpacks <small> (&#9733; 1,985 / [Repository](https://github.com/buildpacks/pack) / [Homepage](https://buildpacks.io/))</small>
- Tanka <small> (&#9733; 1,966 / [Repository](https://github.com/grafana/tanka) / [Homepage](https://tanka.dev/))</small>
- sealer <small> (&#9733; 1,827 / [Repository](https://github.com/alibaba/sealer) / [Homepage](https://sealer.cool))</small>
- Squash <small> (&#9733; 1,710 / [Repository](https://github.com/solo-io/squash) / [Homepage](https://squash.solo.io/))</small>
- Nocalhost <small> (&#9733; 1,557 / [Repository](https://github.com/nocalhost/nocalhost) / [Homepage](https://nocalhost.dev))</small>
- Carvel <small> (&#9733; 1,359 / [Repository](https://github.com/carvel-dev/ytt) / [Homepage](https://carvel.dev))</small>
- KUDO <small> (&#9733; 1,097 / [Repository](https://github.com/kudobuilder/kudo) / [Homepage](https://kudo.dev/))</small>
- Porter <small> (&#9733; 977 / [Repository](https://github.com/getporter/porter) / [Homepage](https://getporter.org/))</small>
- KOTS <small> (&#9733; 817 / [Repository](https://github.com/replicatedhq/kots) / [Homepage](https://kots.io))</small>
- CloudARK KubePlus <small> (&#9733; 501 / [Repository](https://github.com/cloud-ark/kubeplus) / [Homepage](https://cloudark.io/helm-chart-as-a-service))</small>
- KubeOrbit <small> (&#9733; 454 / [Repository](https://github.com/teamcode-inc/kubeorbit) / [Homepage](https://www.kubeorbit.io/))</small>
- KubeCarrier <small> (&#9733; 286 / [Repository](https://github.com/kubermatic/kubecarrier) / [Homepage](https://github.com/kubermatic/kubecarrier))</small>
- Devfile <small> (&#9733; 159 / [Repository](https://github.com/devfile/api) / [Homepage](https://devfile.io))</small>

### App Definition and Development / Continuous Integration & Delivery
- Drone <small> (&#9733; 26,762 / [Repository](https://github.com/harness/drone) / [Homepage](http://try.drone.io/))</small>
- k6 <small> (&#9733; 20,092 / [Repository](https://github.com/grafana/k6) / [Homepage](https://k6.io))</small>
- Argo <small> (&#9733; 12,791 / [Repository](https://github.com/argoproj/argo-cd) / [Homepage](https://argoproj.github.io/))</small>
- Tekton Pipelines <small> (&#9733; 7,790 / [Repository](https://github.com/tektoncd/pipeline) / [Homepage](https://tekton.dev/))</small>
- Concourse <small> (&#9733; 6,839 / [Repository](https://github.com/concourse/concourse) / [Homepage](https://concourse-ci.org/))</small>
- Bytebase <small> (&#9733; 5,339 / [Repository](https://github.com/bytebase/bytebase) / [Homepage](https://www.bytebase.com/))</small>
- Flux <small> (&#9733; 4,731 / [Repository](https://github.com/fluxcd/flux2) / [Homepage](https://fluxcd.io/))</small>
- JenkinsX <small> (&#9733; 4,366 / [Repository](https://github.com/jenkins-x/jx) / [Homepage](https://jenkins-x.io/))</small>
- Flagger <small> (&#9733; 4,225 / [Repository](https://github.com/fluxcd/flagger) / [Homepage](https://docs.flagger.app))</small>
- OpenKruise <small> (&#9733; 3,807 / [Repository](https://github.com/openkruise/kruise) / [Homepage](https://openkruise.io/en-us/))</small>
- werf <small> (&#9733; 3,599 / [Repository](https://github.com/werf/werf) / [Homepage](https://werf.io/))</small>
- Devtron <small> (&#9733; 3,057 / [Repository](https://github.com/devtron-labs/devtron) / [Homepage](https://devtron.ai))</small>
- Woodpecker CI <small> (&#9733; 2,519 / [Repository](https://github.com/woodpecker-ci/woodpecker) / [Homepage](https://woodpecker-ci.org))</small>
- Brigade <small> (&#9733; 2,383 / [Repository](https://github.com/brigadecore/brigade) / [Homepage](https://brigade.sh/))</small>
- Flipt <small> (&#9733; 2,326 / [Repository](https://github.com/flipt-io/flipt) / [Homepage](https://flipt.io))</small>
- Keploy <small> (&#9733; 1,758 / [Repository](https://github.com/keploy/keploy) / [Homepage](https://keploy.io))</small>
- Keptn <small> (&#9733; 1,725 / [Repository](https://github.com/keptn/keptn) / [Homepage](https://www.keptn.sh))</small>
- Agola <small> (&#9733; 1,269 / [Repository](https://github.com/agola-io/agola) / [Homepage](https://agola.io))</small>
- Testkube <small> (&#9733; 759 / [Repository](https://github.com/kubeshop/testkube) / [Homepage](https://testkube.kubeshop.io))</small>
- PipeCD <small> (&#9733; 684 / [Repository](https://github.com/pipe-cd/pipecd) / [Homepage](https://pipecd.dev/))</small>
- Cartographer <small> (&#9733; 411 / [Repository](https://github.com/vmware-tanzu/cartographer) / [Homepage](https://cartographer.sh/))</small>

### Platform / Certified Kubernetes - Distribution
- k3s <small> (&#9733; 22,860 / [Repository](https://github.com/k3s-io/k3s) / [Homepage](https://k3s.io))</small>
- Rancher Kubernetes <small> (&#9733; 20,908 / [Repository](https://github.com/rancher/rancher) / [Homepage](https://rancher.com))</small>
- Kubesphere <small> (&#9733; 12,466 / [Repository](https://github.com/kubesphere/kubesphere) / [Homepage](https://kubesphere.io))</small>
- vcluster <small> (&#9733; 2,500 / [Repository](https://github.com/loft-sh/vcluster) / [Homepage](https://vcluster.com/))</small>
- RKE Government <small> (&#9733; 939 / [Repository](https://github.com/rancher/rke2) / [Homepage](https://docs.rke2.io/))</small>
- Kubermatic Kubernetes Platform <small> (&#9733; 935 / [Repository](https://github.com/kubermatic/kubermatic) / [Homepage](https://www.kubermatic.com))</small>
- Flant Deckhouse <small> (&#9733; 834 / [Repository](https://github.com/deckhouse/deckhouse) / [Homepage](https://deckhouse.io/en))</small>
- k0s <small> (&#9733; 809 / [Repository](https://github.com/k0sproject/k0s) / [Homepage](https://k0sproject.io))</small>
- KubeCube <small> (&#9733; 376 / [Repository](https://github.com/kubecube-io/KubeCube) / [Homepage](https://www.kubecube.io/))</small>
- Kamaji <small> (&#9733; 331 / [Repository](https://github.com/clastix/kamaji) / [Homepage](https://github.com/clastix/kamaji))</small>
- Red Hat OpenShift <small> (&#9733; 55 / [Repository](https://github.com/openshift/kubernetes) / [Homepage](https://www.redhat.com/en/technologies/cloud-computing/openshift))</small>
- Flexkube <small> (&#9733; 30 / [Repository](https://github.com/flexkube/libflexkube) / [Homepage](https://github.com/flexkube/libflexkube))</small>

### Platform / Certified Kubernetes - Hosted
- Microsoft AKS Engine for Azure Stack <small> (&#9733; 6 / [Repository](https://github.com/msazurestackworkloads/aks-engine) / [Homepage](https://docs.microsoft.com/en-us/azure-stack/user/azure-stack-kubernetes-aks-engine-overview?view=azs-2108))</small>

### Platform / Certified Kubernetes - Installer
- minikube <small> (&#9733; 26,294 / [Repository](https://github.com/kubernetes/minikube) / [Homepage](https://minikube.sigs.k8s.io))</small>
- kOps <small> (&#9733; 14,885 / [Repository](https://github.com/kubernetes/kops) / [Homepage](https://github.com/kubernetes/kops))</small>
- kind <small> (&#9733; 11,444 / [Repository](https://github.com/kubernetes-sigs/kind) / [Homepage](https://github.com/kubernetes-sigs/kind))</small>
- Sidero Talos Linux <small> (&#9733; 3,796 / [Repository](https://github.com/siderolabs/talos) / [Homepage](https://www.sideroLabs.com))</small>
- Rancher Kubernetes Engine (RKE) <small> (&#9733; 2,948 / [Repository](https://github.com/rancher/rke) / [Homepage](https://github.com/rancher/rke))</small>
- Gardener <small> (&#9733; 2,470 / [Repository](https://github.com/gardener/gardener) / [Homepage](https://gardener.cloud))</small>
- Amazon Elastic Kubernetes Service Anywhere (Amazon EKS Anywhere) <small> (&#9733; 1,759 / [Repository](https://github.com/aws/eks-anywhere) / [Homepage](https://aws.amazon.com/eks/eks-anywhere))</small>
- Kubekey <small> (&#9733; 1,544 / [Repository](https://github.com/kubesphere/kubekey) / [Homepage](https://kubesphere.io/docs/installing-on-linux/introduction/kubekey))</small>
- Kubermatic KubeOne <small> (&#9733; 1,232 / [Repository](https://github.com/kubermatic/kubeone) / [Homepage](https://www.kubermatic.com))</small>
- kwok <small> (&#9733; 1,071 / [Repository](https://github.com/kubernetes-sigs/kwok) / [Homepage](https://kwok.sigs.k8s.io))</small>
- Kubernetes - The Easier Way <small> (&#9733; 300 / [Repository](https://github.com/darxkies/k8s-tew) / [Homepage](https://github.com/darxkies/k8s-tew))</small>
- Cybozu Kubernetes Engine <small> (&#9733; 160 / [Repository](https://github.com/cybozu-go/cke) / [Homepage](https://github.com/cybozu-go/cke))</small>
- KubeClipper <small> (&#9733; 138 / [Repository](https://github.com/kubeclipper/kubeclipper) / [Homepage](https://www.kubeclipper.io/))</small>

### Platform / PaaS/Container Service
- Portainer <small> (&#9733; 25,222 / [Repository](https://github.com/portainer/portainer) / [Homepage](https://www.portainer.io/))</small>
- Tsuru <small> (&#9733; 4,310 / [Repository](https://github.com/tsuru/tsuru) / [Homepage](https://tsuru.io/))</small>
- Rio <small> (&#9733; 2,280 / [Repository](https://github.com/rancher/rio) / [Homepage](https://rio.io/))</small>
- Cloud Foundry Application Runtime <small> (&#9733; 1,700 / [Repository](https://github.com/cloudfoundry/cli) / [Homepage](https://www.cloudfoundry.org/working-groups))</small>
- Kyma <small> (&#9733; 1,437 / [Repository](https://github.com/kyma-project/kyma) / [Homepage](https://kyma-project.io))</small>

### Serverless / Framework
- Dapr <small> (&#9733; 20,969 / [Repository](https://github.com/dapr/dapr) / [Homepage](https://dapr.io))</small>
- Encore <small> (&#9733; 3,652 / [Repository](https://github.com/encoredev/encore) / [Homepage](https://encore.dev))</small>
- Layotto <small> (&#9733; 726 / [Repository](https://github.com/mosn/layotto) / [Homepage](https://mosn.io/layotto))</small>
- Nitric <small> (&#9733; 504 / [Repository](https://github.com/nitrictech/nitric) / [Homepage](https://nitric.io/))</small>

### Serverless / Installable Platform
- OpenFaaS <small> (&#9733; 22,962 / [Repository](https://github.com/openfaas/faas) / [Homepage](https://www.openfaas.com))</small>
- Fission <small> (&#9733; 7,615 / [Repository](https://github.com/fission/fission) / [Homepage](https://fission.io/))</small>
- Kubeless <small> (&#9733; 6,869 / [Repository](https://github.com/vmware-archive/kubeless) / [Homepage](https://github.com/vmware-archive/kubeless-website))</small>
- Keda <small> (&#9733; 6,227 / [Repository](https://github.com/kedacore/keda) / [Homepage](https://keda.sh/))</small>
- Nuclio <small> (&#9733; 4,817 / [Repository](https://github.com/nuclio/nuclio) / [Homepage](https://nuclio.io/))</small>
- Virtual Kubelet <small> (&#9733; 3,787 / [Repository](https://github.com/virtual-kubelet/virtual-kubelet) / [Homepage](https://virtual-kubelet.io/))</small>
- OpenFunction <small> (&#9733; 1,123 / [Repository](https://github.com/OpenFunction/OpenFunction) / [Homepage](https://openfunction.dev))</small>
- Apache Camel K <small> (&#9733; 767 / [Repository](https://github.com/apache/camel-k) / [Homepage](https://camel.apache.org))</small>
- Knative <small> (&#9733; 209 / [Repository](https://github.com/knative/community) / [Homepage](https://knative.dev))</small>

### Observability and Analysis / Monitoring
- Prometheus <small> (&#9733; 47,774 / [Repository](https://github.com/prometheus/prometheus) / [Homepage](https://prometheus.io/))</small>
- InfluxData <small> (&#9733; 25,283 / [Repository](https://github.com/influxdata/influxdb) / [Homepage](https://www.influxdata.com/))</small>
- Thanos <small> (&#9733; 11,639 / [Repository](https://github.com/thanos-io/thanos) / [Homepage](https://thanos.io/))</small>
- Beats <small> (&#9733; 11,613 / [Repository](https://github.com/elastic/beats) / [Homepage](https://www.elastic.co/beats))</small>
- VictoriaMetrics <small> (&#9733; 8,367 / [Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) / [Homepage](https://victoriametrics.com/))</small>
- Falcon <small> (&#9733; 7,056 / [Repository](https://github.com/open-falcon/falcon-plus) / [Homepage](https://open-falcon.com))</small>
- Nightingale <small> (&#9733; 6,293 / [Repository](https://github.com/didi/nightingale) / [Homepage](http://n9e.didiyun.com))</small>
- Weave Scope <small> (&#9733; 5,686 / [Repository](https://github.com/weaveworks/scope) / [Homepage](https://www.weave.works/oss/scope/))</small>
- Cortex <small> (&#9733; 5,046 / [Repository](https://github.com/cortexproject/cortex) / [Homepage](https://cortexmetrics.io/))</small>
- M3 <small> (&#9733; 4,407 / [Repository](https://github.com/m3db/m3) / [Homepage](https://www.m3db.io/))</small>
- Kiali <small> (&#9733; 3,082 / [Repository](https://github.com/kiali/kiali) / [Homepage](https://www.kiali.io/))</small>
- Grafana Mimir <small> (&#9733; 3,058 / [Repository](https://github.com/grafana/mimir) / [Homepage](https://grafana.com/oss/mimir))</small>
- LinDB <small> (&#9733; 2,656 / [Repository](https://github.com/lindb/lindb) / [Homepage](https://www.lindb.io/))</small>
- Hubble <small> (&#9733; 2,621 / [Repository](https://github.com/cilium/hubble) / [Homepage](https://github.com/cilium/hubble))</small>
- K8sGPT <small> (&#9733; 2,539 / [Repository](https://github.com/k8sgpt-ai/k8sgpt) / [Homepage](https://www.k8sgpt.ai))</small>
- OpenMetrics <small> (&#9733; 2,044 / [Repository](https://github.com/OpenObservability/OpenMetrics) / [Homepage](https://openmetrics.io/))</small>
- Grafana Phlare <small> (&#9733; 2,034 / [Repository](https://github.com/grafana/phlare) / [Homepage](https://grafana.com/oss/phlare))</small>
- Trickster <small> (&#9733; 1,872 / [Repository](https://github.com/trickstercache/trickster) / [Homepage](https://trickstercache.org))</small>
- Botkube <small> (&#9733; 1,742 / [Repository](https://github.com/kubeshop/botkube) / [Homepage](https://www.botkube.io))</small>
- Kuberhealthy <small> (&#9733; 1,681 / [Repository](https://github.com/kuberhealthy/kuberhealthy) / [Homepage](https://github.com/kuberhealthy/kuberhealthy))</small>
- Promscale <small> (&#9733; 1,324 / [Repository](https://github.com/timescale/promscale) / [Homepage](https://timescale.com/promscale))</small>
- Sensu <small> (&#9733; 875 / [Repository](https://github.com/sensu/sensu-go) / [Homepage](https://sensu.io/))</small>
- DeepFlow <small> (&#9733; 826 / [Repository](https://github.com/deepflowys/deepflow) / [Homepage](https://deepflow.yunshan.net/community.html))</small>
- NexClipper <small> (&#9733; 559 / [Repository](https://github.com/NexClipper/NexClipper) / [Homepage](https://www.nexclipper.io/))</small>
- Kepler <small> (&#9733; 503 / [Repository](https://github.com/sustainable-computing-io/kepler) / [Homepage](https://sustainable-computing.io/))</small>

### Observability and Analysis / Logging
- Grafana Loki <small> (&#9733; 18,861 / [Repository](https://github.com/grafana/loki) / [Homepage](https://grafana.com/oss/loki))</small>
- Loggie <small> (&#9733; 938 / [Repository](https://github.com/loggie-io/loggie) / [Homepage](https://loggie-io.github.io/))</small>

### Observability and Analysis / Tracing
- Jaeger <small> (&#9733; 17,481 / [Repository](https://github.com/jaegertracing/jaeger) / [Homepage](https://www.jaegertracing.io/))</small>
- OpenTracing <small> (&#9733; 3,459 / [Repository](https://github.com/opentracing/opentracing-go) / [Homepage](https://opentracing.io/))</small>
- Grafana Tempo <small> (&#9733; 2,922 / [Repository](https://github.com/grafana/tempo) / [Homepage](https://grafana.com/oss/tempo/))</small>
- Elastic APM <small> (&#9733; 1,093 / [Repository](https://github.com/elastic/apm-server) / [Homepage](https://www.elastic.co/observability/application-performance-monitoring))</small>
- Teletrace <small> (&#9733; 535 / [Repository](https://github.com/teletrace/teletrace) / [Homepage](https://docs.teletrace.io/))</small>
- Tracetest <small> (&#9733; 504 / [Repository](https://github.com/kubeshop/tracetest) / [Homepage](https://tracetest.io))</small>

### Observability and Analysis / Chaos Engineering
- Chaos Mesh <small> (&#9733; 5,631 / [Repository](https://github.com/chaos-mesh/chaos-mesh) / [Homepage](https://chaos-mesh.org/))</small>
- Chaosblade <small> (&#9733; 5,275 / [Repository](https://github.com/chaosblade-io/chaosblade) / [Homepage](https://chaosblade.io/))</small>
- chaoskube <small> (&#9733; 1,626 / [Repository](https://github.com/linki/chaoskube) / [Homepage](https://github.com/linki/chaoskube))</small>

### Observability and Analysis / Continuous Optimization
- Infracost <small> (&#9733; 8,925 / [Repository](https://github.com/infracost/infracost) / [Homepage](https://www.infracost.io/))</small>
- Kubecost <small> (&#9733; 3,620 / [Repository](https://github.com/kubecost/cost-model) / [Homepage](https://www.kubecost.com/))</small>
- OpenCost <small> (&#9733; 3,620 / [Repository](https://github.com/opencost/opencost) / [Homepage](https://www.opencost.io/))</small>
- gocrane <small> (&#9733; 1,346 / [Repository](https://github.com/gocrane/crane) / [Homepage](https://gocrane.io/))</small>

### Wasm / Toolchain
- Subo CLI <small> (&#9733; 73 / [Repository](https://github.com/suborbital/subo) / [Homepage](https://github.com/suborbital/subo))</small>

### Wasm / Packaging, Registries & Application Delivery
- OCI <small> (&#9733; 10,257 / [Repository](https://github.com/opencontainers/runc) / [Homepage](https://opencontainers.org/))</small>

### Wasm / Installable Platform
- Atmo <small> (&#9733; 680 / [Repository](https://github.com/suborbital/atmo) / [Homepage](https://docs.suborbital.dev/atmo))</small>

## <span style="color:#b07219;">&#9679;</span> Java <small>(71 projects)</small>

### Provisioning / Automation & Configuration
- Apollo <small> (&#9733; 27,977 / [Repository](https://github.com/apolloconfig/apollo) / [Homepage](https://www.apolloconfig.com/))</small>

### Provisioning / Security & Compliance
- Keycloak <small> (&#9733; 15,747 / [Repository](https://github.com/keycloak/keycloak) / [Homepage](https://www.keycloak.org/))</small>
- Paladin Cloud <small> (&#9733; 498 / [Repository](https://github.com/PaladinCloud/CE) / [Homepage](https://paladincloud.io/))</small>

### Provisioning / Key Management
- Square Keywhiz <small> (&#9733; 2,577 / [Repository](https://github.com/square/keywhiz) / [Homepage](https://square.github.io/keywhiz/))</small>
- Athenz <small> (&#9733; 765 / [Repository](https://github.com/AthenZ/athenz) / [Homepage](https://www.athenz.io))</small>

### Runtime / Cloud Native Storage
- Alluxio <small> (&#9733; 6,185 / [Repository](https://github.com/alluxio/alluxio) / [Homepage](https://www.alluxio.io/))</small>
- LINSTOR <small> (&#9733; 678 / [Repository](https://github.com/LINBIT/linstor-server) / [Homepage](https://www.linbit.com/linstor/))</small>

### Orchestration & Management / Scheduling & Orchestration
- DolphinScheduler <small> (&#9733; 10,327 / [Repository](https://github.com/apache/dolphinscheduler) / [Homepage](https://dolphinscheduler.apache.org))</small>

### Orchestration & Management / Coordination & Service Discovery
- Nacos <small> (&#9733; 26,123 / [Repository](https://github.com/alibaba/nacos) / [Homepage](https://nacos.io/en-us/))</small>
- Netflix Eureka <small> (&#9733; 11,781 / [Repository](https://github.com/Netflix/eureka) / [Homepage](https://github.com/Netflix/eureka))</small>
- Apache Zookeeper <small> (&#9733; 11,208 / [Repository](https://github.com/apache/zookeeper) / [Homepage](https://zookeeper.apache.org/))</small>

### Orchestration & Management / Remote Procedure Call
- Dubbo <small> (&#9733; 38,780 / [Repository](https://github.com/apache/dubbo) / [Homepage](https://dubbo.apache.org/en/))</small>
- SOFARPC <small> (&#9733; 3,680 / [Repository](https://github.com/sofastack/sofa-rpc) / [Homepage](https://www.sofastack.tech/en/))</small>
- Avro <small> (&#9733; 2,467 / [Repository](https://github.com/apache/avro) / [Homepage](https://avro.apache.org/))</small>

### Orchestration & Management / Service Proxy
- Sentinel <small> (&#9733; 20,853 / [Repository](https://github.com/alibaba/Sentinel) / [Homepage](https://sentinelguard.io/en-us/))</small>
- Netflix Zuul <small> (&#9733; 12,565 / [Repository](https://github.com/Netflix/zuul) / [Homepage](https://github.com/Netflix/zuul))</small>

### Orchestration & Management / API Gateway
- Gravitee.io <small> (&#9733; 1,592 / [Repository](https://github.com/gravitee-io/gravitee-api-management) / [Homepage](https://gravitee.io))</small>
- MuleSoft <small> (&#9733; 354 / [Repository](https://github.com/mulesoft/mule) / [Homepage](https://www.mulesoft.com/))</small>
- WSO2 API Microgateway <small> (&#9733; 234 / [Repository](https://github.com/wso2/product-microgateway) / [Homepage](https://wso2.com/api-manager/api-microgateway))</small>

### Orchestration & Management / Service Mesh
- Sermant <small> (&#9733; 499 / [Repository](https://github.com/huaweicloud/Sermant) / [Homepage](https://sermant.io/))</small>

### App Definition and Development / Database
- Seata <small> (&#9733; 23,656 / [Repository](https://github.com/seata/seata) / [Homepage](https://seata.io/en-us))</small>
- ShardingSphere <small> (&#9733; 18,275 / [Repository](https://github.com/apache/shardingsphere) / [Homepage](https://shardingsphere.apache.org/))</small>
- Presto <small> (&#9733; 14,639 / [Repository](https://github.com/prestodb/presto) / [Homepage](https://prestodb.io/))</small>
- Apache Hadoop <small> (&#9733; 13,447 / [Repository](https://github.com/apache/hadoop) / [Homepage](https://hadoop.apache.org/))</small>
- Druid <small> (&#9733; 12,558 / [Repository](https://github.com/apache/druid) / [Homepage](https://druid.apache.org/))</small>
- Neo4j <small> (&#9733; 11,298 / [Repository](https://github.com/neo4j/neo4j) / [Homepage](https://neo4j.com))</small>
- Cassandra <small> (&#9733; 7,937 / [Repository](https://github.com/apache/cassandra) / [Homepage](https://cassandra.apache.org/_/index.html))</small>
- Doris <small> (&#9733; 7,887 / [Repository](https://github.com/apache/doris) / [Homepage](https://doris.apache.org/))</small>
- Hazelcast IMDG <small> (&#9733; 5,323 / [Repository](https://github.com/hazelcast/hazelcast) / [Homepage](https://hazelcast.com/open-source-projects))</small>
- OrientDB <small> (&#9733; 4,575 / [Repository](https://github.com/orientechnologies/orientdb) / [Homepage](https://orientdb.com/why-orientdb/))</small>
- Apache Ignite <small> (&#9733; 4,431 / [Repository](https://github.com/apache/ignite) / [Homepage](https://ignite.apache.org))</small>
- Crate.io <small> (&#9733; 3,658 / [Repository](https://github.com/crate/crate) / [Homepage](https://crate.io/))</small>
- VoltDB <small> (&#9733; 1,991 / [Repository](https://github.com/voltdb/voltdb) / [Homepage](https://www.voltactivedata.com))</small>
- Infinispan <small> (&#9733; 1,039 / [Repository](https://github.com/infinispan/infinispan) / [Homepage](https://infinispan.org/))</small>
- Scalar DB <small> (&#9733; 365 / [Repository](https://github.com/scalar-labs/scalardb) / [Homepage](https://scalar-labs.com/))</small>

### App Definition and Development / Streaming & Messaging
- Kafka <small> (&#9733; 24,707 / [Repository](https://github.com/apache/kafka) / [Homepage](https://kafka.apache.org/))</small>
- Flink <small> (&#9733; 21,095 / [Repository](https://github.com/apache/flink) / [Homepage](https://flink.apache.org/))</small>
- Apache RocketMQ <small> (&#9733; 19,133 / [Repository](https://github.com/apache/rocketmq) / [Homepage](https://rocketmq.apache.org/))</small>
- Pulsar <small> (&#9733; 12,571 / [Repository](https://github.com/apache/pulsar) / [Homepage](https://pulsar.apache.org/))</small>
- Beam <small> (&#9733; 6,765 / [Repository](https://github.com/apache/beam) / [Homepage](https://beam.apache.org/))</small>
- Apache Storm <small> (&#9733; 6,444 / [Repository](https://github.com/apache/storm) / [Homepage](https://storm.apache.org/))</small>
- SeaTunnel <small> (&#9733; 5,012 / [Repository](https://github.com/apache/incubator-seatunnel) / [Homepage](https://seatunnel.apache.org/))</small>
- Strimzi <small> (&#9733; 4,389 / [Repository](https://github.com/strimzi/strimzi-kafka-operator) / [Homepage](https://strimzi.io/))</small>
- Apache NiFi <small> (&#9733; 3,738 / [Repository](https://github.com/apache/nifi) / [Homepage](https://nifi.apache.org/))</small>
- Apache Heron <small> (&#9733; 3,649 / [Repository](https://github.com/apache/incubator-heron) / [Homepage](https://apache.github.io/incubator-heron/))</small>
- Pravega <small> (&#9733; 1,865 / [Repository](https://github.com/pravega/pravega) / [Homepage](https://cncf.pravega.io))</small>
- Siddhi <small> (&#9733; 1,431 / [Repository](https://github.com/siddhi-io/siddhi) / [Homepage](https://siddhi.io/))</small>
- Hazelcast Jet <small> (&#9733; 1,056 / [Repository](https://github.com/hazelcast/hazelcast-jet) / [Homepage](https://jet-start.sh))</small>
- OpenMessaging <small> (&#9733; 716 / [Repository](https://github.com/openmessaging/openmessaging-java) / [Homepage](https://openmessaging.cloud))</small>
- StreamSets <small> (&#9733; 56 / [Repository](https://github.com/streamsets/datacollector-oss) / [Homepage](https://streamsets.com/))</small>

### App Definition and Development / Application Definition & Image Build
- ServiceComb <small> (&#9733; 1,848 / [Repository](https://github.com/apache/servicecomb-java-chassis) / [Homepage](https://servicecomb.apache.org))</small>

### App Definition and Development / Continuous Integration & Delivery
- Jenkins <small> (&#9733; 20,660 / [Repository](https://github.com/jenkinsci/jenkins) / [Homepage](https://jenkins.io/))</small>
- GoCD <small> (&#9733; 6,763 / [Repository](https://github.com/gocd/gocd) / [Homepage](https://www.gocd.org/))</small>
- Liquibase <small> (&#9733; 3,810 / [Repository](https://github.com/liquibase/liquibase) / [Homepage](https://www.liquibase.com/))</small>
- HyScale <small> (&#9733; 439 / [Repository](https://github.com/hyscale/hyscale) / [Homepage](https://www.hyscale.io))</small>

### Serverless / Framework
- EventMesh <small> (&#9733; 1,307 / [Repository](https://github.com/apache/incubator-eventmesh) / [Homepage](https://eventmesh.apache.org/))</small>
- Spring Cloud Function <small> (&#9733; 963 / [Repository](https://github.com/spring-cloud/spring-cloud-function) / [Homepage](https://spring.io/projects/spring-cloud-function))</small>
- Stateful Functions <small> (&#9733; 437 / [Repository](https://github.com/apache/flink-statefun) / [Homepage](https://statefun.io))</small>

### Observability and Analysis / Monitoring
- OpenTSDB <small> (&#9733; 4,821 / [Repository](https://github.com/OpenTSDB/opentsdb) / [Homepage](http://opentsdb.net/))</small>
- Micrometer <small> (&#9733; 3,956 / [Repository](https://github.com/micrometer-metrics/micrometer) / [Homepage](https://micrometer.io/))</small>
- Sidekick <small> (&#9733; 1,663 / [Repository](https://github.com/runsidekick/sidekick) / [Homepage](https://www.runsidekick.com/))</small>

### Observability and Analysis / Logging
- Elastic <small> (&#9733; 63,438 / [Repository](https://github.com/elastic/elasticsearch) / [Homepage](https://www.elastic.co/))</small>
- Logstash <small> (&#9733; 13,408 / [Repository](https://github.com/elastic/logstash) / [Homepage](https://www.elastic.co/logstash))</small>
- OpenSearch <small> (&#9733; 6,761 / [Repository](https://github.com/opensearch-project/opensearch) / [Homepage](https://opensearch.org))</small>
- Graylog <small> (&#9733; 6,513 / [Repository](https://github.com/Graylog2/graylog2-server) / [Homepage](https://www.graylog.org/))</small>

### Observability and Analysis / Tracing
- SkyWalking <small> (&#9733; 21,668 / [Repository](https://github.com/apache/skywalking) / [Homepage](https://skywalking.apache.org/))</small>
- Zipkin <small> (&#9733; 16,118 / [Repository](https://github.com/openzipkin/zipkin) / [Homepage](https://zipkin.io/))</small>
- Pinpoint <small> (&#9733; 12,712 / [Repository](https://github.com/pinpoint-apm/pinpoint) / [Homepage](https://naver.github.io/pinpoint/))</small>
- Spring Cloud Sleuth <small> (&#9733; 1,687 / [Repository](https://github.com/spring-cloud/spring-cloud-sleuth) / [Homepage](https://spring.io/projects/spring-cloud-sleuth))</small>
- SOFATracer <small> (&#9733; 1,047 / [Repository](https://github.com/sofastack/sofa-tracer) / [Homepage](https://www.sofastack.tech/en/))</small>
- EaseAgent <small> (&#9733; 516 / [Repository](https://github.com/megaease/easeagent) / [Homepage](https://github.com/megaease/easeagent))</small>

## <span style="color:#3572A5;">&#9679;</span> Python <small>(39 projects)</small>

### Provisioning / Automation & Configuration
- Ansible <small> (&#9733; 57,092 / [Repository](https://github.com/ansible/ansible) / [Homepage](https://www.ansible.com/))</small>
- SaltStack <small> (&#9733; 13,157 / [Repository](https://github.com/saltstack/salt) / [Homepage](https://www.vmware.com/support/acquisitions/saltstack.html))</small>
- Cloud Custodian <small> (&#9733; 4,766 / [Repository](https://github.com/cloud-custodian/cloud-custodian) / [Homepage](https://cloudcustodian.io/))</small>
- OpenStack <small> (&#9733; 4,754 / [Repository](https://github.com/openstack/openstack) / [Homepage](https://www.openstack.org/))</small>
- CDK for Kubernetes (CDK8s) <small> (&#9733; 3,589 / [Repository](https://github.com/cdk8s-team/cdk8s) / [Homepage](https://cdk8s.io/))</small>
- Mist.io <small> (&#9733; 1,741 / [Repository](https://github.com/mistio/mist-ce) / [Homepage](https://mist.io/))</small>
- Couler <small> (&#9733; 804 / [Repository](https://github.com/couler-proj/couler) / [Homepage](https://couler-proj.github.io/couler/index.html))</small>
- MAAS <small> (&#9733; 252 / [Repository](https://github.com/maas/maas) / [Homepage](https://maas.io/))</small>
- Cloudify <small> (&#9733; 136 / [Repository](https://github.com/cloudify-cosmo/cloudify-manager) / [Homepage](https://cloudify.co))</small>

### Provisioning / Container Registry
- Quay <small> (&#9733; 2,167 / [Repository](https://github.com/quay/quay) / [Homepage](https://quay.io/))</small>

### Provisioning / Security & Compliance
- Checkov <small> (&#9733; 5,497 / [Repository](https://github.com/bridgecrewio/checkov) / [Homepage](https://www.checkov.io/))</small>
- kube-hunter <small> (&#9733; 4,216 / [Repository](https://github.com/aquasecurity/kube-hunter) / [Homepage](https://github.com/aquasecurity/kube-hunter))</small>
- Anchore <small> (&#9733; 1,536 / [Repository](https://github.com/anchore/anchore-engine) / [Homepage](https://anchore.com/platform))</small>
- The Update Framework (TUF) <small> (&#9733; 1,500 / [Repository](https://github.com/theupdateframework/python-tuf) / [Homepage](https://theupdateframework.github.io/))</small>
- Metarget <small> (&#9733; 776 / [Repository](https://github.com/Metarget/metarget) / [Homepage](https://github.com/Metarget/metarget))</small>
- in-toto <small> (&#9733; 706 / [Repository](https://github.com/in-toto/in-toto) / [Homepage](https://in-toto.io))</small>
- Keylime <small> (&#9733; 318 / [Repository](https://github.com/keylime/keylime) / [Homepage](https://keylime.dev/))</small>
- CloudMatos <small> (&#9733; 9 / [Repository](https://github.com/cloudmatos/matos) / [Homepage](https://www.cloudmatos.com))</small>

### Runtime / Cloud Native Storage
- Swift <small> (&#9733; 2,413 / [Repository](https://github.com/openstack/swift) / [Homepage](https://docs.openstack.org/swift/latest/))</small>
- OpenIO <small> (&#9733; 591 / [Repository](https://github.com/open-io/oio-sds) / [Homepage](https://www.openio.io/))</small>

### Orchestration & Management / Scheduling & Orchestration
- Prefect <small> (&#9733; 11,766 / [Repository](https://github.com/PrefectHQ/prefect) / [Homepage](https://docs.prefect.io/))</small>
- StackStorm <small> (&#9733; 5,486 / [Repository](https://github.com/stackstorm/st2) / [Homepage](https://stackstorm.com/))</small>

### Orchestration & Management / API Gateway
- Emissary-Ingress <small> (&#9733; 4,046 / [Repository](https://github.com/emissary-ingress/emissary) / [Homepage](https://www.getambassador.io/))</small>
- Hango <small> (&#9733; 407 / [Repository](https://github.com/hango-io/hango-gateway) / [Homepage](https://github.com/hango-io))</small>

### App Definition and Development / Database
- BigchainDB <small> (&#9733; 3,974 / [Repository](https://github.com/bigchaindb/bigchaindb) / [Homepage](https://www.bigchaindb.com/))</small>

### App Definition and Development / Application Definition & Image Build
- Gefyra <small> (&#9733; 463 / [Repository](https://github.com/gefyrahq/gefyra) / [Homepage](https://gefyra.dev/))</small>

### Platform / Certified Kubernetes - Distribution
- MicroK8s <small> (&#9733; 7,350 / [Repository](https://github.com/canonical/microk8s) / [Homepage](https://microk8s.io))</small>
- Canonical Charmed Kubernetes <small> (&#9733; 135 / [Repository](https://github.com/charmed-kubernetes/bundle) / [Homepage](https://ubuntu.com/kubernetes))</small>
- Wind River Studio Cloud Platform <small> (&#9733; 1 / [Repository](https://github.com/wind-river/starlingx-config) / [Homepage](https://www.windriver.com/studio/operator/cloud-platform))</small>

### Platform / Certified Kubernetes - Hosted
- Catalyst Kubernetes Service <small> (&#9733; 2 / [Repository](https://github.com/catalyst-cloud/magnum) / [Homepage](https://catalystcloud.nz/services/paas/kubernetes/))</small>

### Platform / PaaS/Container Service
- PaaSTA <small> (&#9733; 1,649 / [Repository](https://github.com/Yelp/paasta) / [Homepage](https://engineeringblog.yelp.com/2015/11/introducing-paasta-an-open-platform-as-a-service.html))</small>

### Serverless / Tools
- SCAR <small> (&#9733; 587 / [Repository](https://github.com/grycap/scar) / [Homepage](https://scar.readthedocs.io/en/latest/))</small>

### Serverless / Framework
- Chalice <small> (&#9733; 9,683 / [Repository](https://github.com/aws/chalice) / [Homepage](https://aws.amazon.com/blogs/developer/chalice-1-0-0-ga-release/))</small>
- AWS Server Application Model (SAM) <small> (&#9733; 8,996 / [Repository](https://github.com/aws/serverless-application-model) / [Homepage](https://aws.amazon.com/serverless/sam/))</small>

### Serverless / Installable Platform
- AppScale <small> (&#9733; 2,424 / [Repository](https://github.com/AppScale/gts) / [Homepage](https://www.appscale.com/))</small>

### Observability and Analysis / Monitoring
- Sentry <small> (&#9733; 33,961 / [Repository](https://github.com/getsentry/sentry) / [Homepage](https://sentry.io/welcome/))</small>
- Checkmk <small> (&#9733; 999 / [Repository](https://github.com/tribe29/checkmk) / [Homepage](https://checkmk.com/))</small>

### Observability and Analysis / Chaos Engineering
- PowerfulSeal <small> (&#9733; 1,864 / [Repository](https://github.com/powerfulseal/powerfulseal) / [Homepage](https://github.com/powerfulseal/powerfulseal))</small>
- Chaos Toolkit <small> (&#9733; 1,699 / [Repository](https://github.com/chaostoolkit/chaostoolkit) / [Homepage](https://chaostoolkit.org/))</small>

## <span style="color:#f34b7d;">&#9679;</span> C++ <small>(37 projects)</small>

### Provisioning / Security & Compliance
- Falco <small> (&#9733; 5,806 / [Repository](https://github.com/falcosecurity/falco) / [Homepage](https://falco.org/))</small>

### Runtime / Cloud Native Storage
- Ceph <small> (&#9733; 11,780 / [Repository](https://github.com/ceph/ceph) / [Homepage](https://ceph.io/en))</small>
- Rook <small> (&#9733; 11,305 / [Repository](https://github.com/rook/rook) / [Homepage](https://rook.io/))</small>
- CubeFS <small> (&#9733; 3,211 / [Repository](https://github.com/cubeFS/cubefs) / [Homepage](https://cubefs.io/))</small>
- Curve <small> (&#9733; 1,840 / [Repository](https://github.com/opencurve/curve) / [Homepage](http://www.opencurve.io/))</small>
- Vineyard <small> (&#9733; 713 / [Repository](https://github.com/v6d-io/v6d) / [Homepage](https://v6d.io))</small>

### Runtime / Container Runtime
- WasmEdge Runtime <small> (&#9733; 5,812 / [Repository](https://github.com/WasmEdge/WasmEdge) / [Homepage](https://wasmedge.org/))</small>

### Orchestration & Management / Scheduling & Orchestration
- Apache Mesos <small> (&#9733; 5,047 / [Repository](https://github.com/apache/mesos) / [Homepage](https://mesos.apache.org/))</small>
- Azure Service Fabric <small> (&#9733; 2,962 / [Repository](https://github.com/Microsoft/service-fabric) / [Homepage](https://docs.microsoft.com/en-us/azure/service-fabric/))</small>

### Orchestration & Management / Remote Procedure Call
- gRPC <small> (&#9733; 37,659 / [Repository](https://github.com/grpc/grpc) / [Homepage](https://grpc.io/))</small>
- Apache Thrift <small> (&#9733; 9,661 / [Repository](https://github.com/apache/thrift) / [Homepage](https://thrift.apache.org/))</small>
- TARS <small> (&#9733; 9,611 / [Repository](https://github.com/tarsCloud/tars) / [Homepage](https://github.com/tarsCloud))</small>
- SRPC <small> (&#9733; 1,603 / [Repository](https://github.com/sogou/srpc) / [Homepage](https://github.com/sogou/srpc))</small>

### Orchestration & Management / Service Proxy
- Envoy <small> (&#9733; 21,858 / [Repository](https://github.com/envoyproxy/envoy) / [Homepage](https://www.envoyproxy.io))</small>
- Pipy <small> (&#9733; 583 / [Repository](https://github.com/flomesh-io/pipy) / [Homepage](https://flomesh.io/pipy/))</small>

### Orchestration & Management / API Gateway
- Higress <small> (&#9733; 1,099 / [Repository](https://github.com/alibaba/higress) / [Homepage](https://higress.io))</small>

### App Definition and Development / Database
- ClickHouse <small> (&#9733; 28,228 / [Repository](https://github.com/ClickHouse/ClickHouse) / [Homepage](https://clickhouse.com))</small>
- RethinkDB <small> (&#9733; 26,038 / [Repository](https://github.com/rethinkdb/rethinkdb) / [Homepage](https://rethinkdb.com/))</small>
- MongoDB <small> (&#9733; 23,583 / [Repository](https://github.com/mongodb/mongo) / [Homepage](https://www.mongodb.com/))</small>
- DragonflyDB <small> (&#9733; 19,041 / [Repository](https://github.com/dragonflydb/dragonfly) / [Homepage](https://dragonflydb.io/))</small>
- ArangoDB <small> (&#9733; 12,909 / [Repository](https://github.com/arangodb/arangodb) / [Homepage](https://www.arangodb.com/))</small>
- FoundationDB <small> (&#9733; 12,276 / [Repository](https://github.com/apple/foundationdb) / [Homepage](https://www.foundationdb.org/))</small>
- Scylla <small> (&#9733; 9,766 / [Repository](https://github.com/scylladb/scylla) / [Homepage](https://www.scylladb.com/))</small>
- NebulaGraph <small> (&#9733; 8,992 / [Repository](https://github.com/vesoft-inc/nebula) / [Homepage](https://nebula-graph.io/))</small>
- MySQL <small> (&#9733; 8,980 / [Repository](https://github.com/mysql/mysql-server) / [Homepage](https://www.oracle.com/mysql/))</small>
- OceanBase <small> (&#9733; 5,558 / [Repository](https://github.com/oceanbase/oceanbase) / [Homepage](https://en.oceanbase.com/))</small>
- MariaDB <small> (&#9733; 4,790 / [Repository](https://github.com/MariaDB/server) / [Homepage](https://mariadb.com/))</small>
- Percona Server for MySQL <small> (&#9733; 1,002 / [Repository](https://github.com/percona/percona-server) / [Homepage](https://www.percona.com/software/mysql-database/percona-server))</small>
- openGauss <small> (&#9733; 513 / [Repository](https://github.com/opengauss-mirror/openGauss-server) / [Homepage](https://opengauss.org/))</small>

### App Definition and Development / Streaming & Messaging
- Redpanda <small> (&#9733; 6,532 / [Repository](https://github.com/redpanda-data/redpanda) / [Homepage](https://redpanda.com/platform))</small>

### Platform / PaaS/Container Service
- Sogou C++ Workflow <small> (&#9733; 10,508 / [Repository](https://github.com/sogou/workflow) / [Homepage](https://github.com/sogou/workflow))</small>

### Observability and Analysis / Monitoring
- Pixie <small> (&#9733; 4,494 / [Repository](https://github.com/pixie-io/pixie) / [Homepage](https://px.dev/))</small>
- Icinga <small> (&#9733; 1,834 / [Repository](https://github.com/Icinga/icinga2) / [Homepage](https://icinga.com/))</small>
- Netis <small> (&#9733; 920 / [Repository](https://github.com/Netis/packet-agent) / [Homepage](https://wordpress.com/browsehappy))</small>

### Wasm / Runtime
- V8 <small> (&#9733; 21,085 / [Repository](https://github.com/v8/v8) / [Homepage](https://v8.dev/))</small>
- WasmEdge <small> (&#9733; 5,812 / [Repository](https://github.com/WasmEdge/WasmEdge) / [Homepage](https://wasmedge.org/))</small>
- WAVM <small> (&#9733; 2,401 / [Repository](https://github.com/WAVM/WAVM) / [Homepage](https://wavm.github.io))</small>

## <span style="color:#dea584;">&#9679;</span> Rust <small>(27 projects)</small>

### Provisioning / Automation & Configuration
- Akri <small> (&#9733; 938 / [Repository](https://github.com/project-akri/akri) / [Homepage](https://docs.akri.sh))</small>

### Provisioning / Security & Compliance
- Matano <small> (&#9733; 1,029 / [Repository](https://github.com/matanolabs/matano) / [Homepage](https://www.matano.dev))</small>
- Curiefense <small> (&#9733; 615 / [Repository](https://github.com/curiefense/curiefense) / [Homepage](https://www.curiefense.io/))</small>
- Parsec <small> (&#9733; 404 / [Repository](https://github.com/parallaxsecond/parsec) / [Homepage](https://parsec.community/))</small>

### Runtime / Container Runtime
- Firecracker <small> (&#9733; 21,410 / [Repository](https://github.com/firecracker-microvm/firecracker) / [Homepage](https://firecracker-microvm.github.io/))</small>

### Orchestration & Management / Scheduling & Orchestration
- kube-rs <small> (&#9733; 2,052 / [Repository](https://github.com/kube-rs/kube-rs) / [Homepage](https://kube.rs))</small>
- wasmCloud <small> (&#9733; 847 / [Repository](https://github.com/wasmCloud/wasmCloud) / [Homepage](https://wasmcloud.com))</small>

### App Definition and Development / Database
- TiKV <small> (&#9733; 12,969 / [Repository](https://github.com/tikv/tikv) / [Homepage](https://tikv.org))</small>
- Databend <small> (&#9733; 5,848 / [Repository](https://github.com/datafuselabs/databend) / [Homepage](https://databend.rs))</small>
- GreptimeDB <small> (&#9733; 2,600 / [Repository](https://github.com/grepTimeTeam/greptimedb) / [Homepage](https://greptime.com/))</small>
- GraphScope <small> (&#9733; 2,365 / [Repository](https://github.com/alibaba/graphscope) / [Homepage](https://graphscope.io/))</small>

### App Definition and Development / Streaming & Messaging
- Fluvio <small> (&#9733; 1,746 / [Repository](https://github.com/infinyon/fluvio) / [Homepage](https://fluvio.io/))</small>
- Tremor <small> (&#9733; 736 / [Repository](https://github.com/tremor-rs/tremor-runtime) / [Homepage](https://www.tremor.rs/))</small>

### App Definition and Development / Application Definition & Image Build
- Chef Habitat <small> (&#9733; 2,459 / [Repository](https://github.com/habitat-sh/habitat) / [Homepage](https://community.chef.io/tools/chef-habitat))</small>
- mirrord <small> (&#9733; 2,384 / [Repository](https://github.com/metalbear-co/mirrord) / [Homepage](https://www.mirrord.dev/))</small>
- Krator <small> (&#9733; 116 / [Repository](https://github.com/krator-rs/krator) / [Homepage](https://docs.rs/crate/krator/latest))</small>

### Serverless / Installable Platform
- Krustlet <small> (&#9733; 3,378 / [Repository](https://github.com/krustlet/krustlet) / [Homepage](https://krustlet.dev))</small>

### Observability and Analysis / Monitoring
- Vector <small> (&#9733; 13,281 / [Repository](https://github.com/vectordotdev/vector) / [Homepage](https://vector.dev/))</small>
- Fonio <small> (&#9733; 399 / [Repository](https://github.com/foniod/foniod) / [Homepage](https://ingraind.org/))</small>

### Observability and Analysis / Logging
- Parseable <small> (&#9733; 1,076 / [Repository](https://github.com/parseablehq/parseable) / [Homepage](https://www.parseable.io))</small>

### Wasm / Specifications
- WASI <small> (&#9733; 3,667 / [Repository](https://github.com/WebAssembly/WASI) / [Homepage](https://wasi.dev))</small>

### Wasm / Runtime
- Wasmer <small> (&#9733; 14,994 / [Repository](https://github.com/wasmerio/wasmer) / [Homepage](https://wasmer.io))</small>
- wasmtime <small> (&#9733; 12,038 / [Repository](https://github.com/bytecodealliance/wasmtime) / [Homepage](https://wasmtime.dev))</small>
- wasmi <small> (&#9733; 1,085 / [Repository](https://github.com/paritytech/wasmi) / [Homepage](https://paritytech.github.io/wasmi))</small>

### Wasm / Toolchain
- wasm-pack <small> (&#9733; 5,100 / [Repository](https://github.com/rustwasm/wasm-pack) / [Homepage](https://rustwasm.github.io/wasm-pack))</small>
- solang <small> (&#9733; 987 / [Repository](https://github.com/hyperledger-labs/solang) / [Homepage](https://solang.readthedocs.io/en/latest))</small>

### Wasm / Installable Platform
- krustlet <small> (&#9733; 3,378 / [Repository](https://github.com/krustlet/krustlet) / [Homepage](https://krustlet.dev/))</small>

## <span style="color:#555555;">&#9679;</span> C <small>(25 projects)</small>

### Provisioning / Automation & Configuration
- CFEngine <small> (&#9733; 430 / [Repository](https://github.com/cfengine/core) / [Homepage](https://cfengine.com/))</small>

### Provisioning / Security & Compliance
- Tetragon <small> (&#9733; 2,226 / [Repository](https://github.com/cilium/tetragon) / [Homepage](https://github.com/cilium/tetragon))</small>

### Runtime / Cloud Native Storage
- Longhorn <small> (&#9733; 5,278 / [Repository](https://github.com/longhorn/longhorn) / [Homepage](https://longhorn.io/))</small>
- Gluster <small> (&#9733; 4,059 / [Repository](https://github.com/gluster/glusterfs) / [Homepage](https://www.gluster.org/))</small>
- MooseFS <small> (&#9733; 1,423 / [Repository](https://github.com/moosefs/moosefs) / [Homepage](https://moosefs.com/))</small>

### Runtime / Container Runtime
- SmartOS <small> (&#9733; 1,497 / [Repository](https://github.com/TritonDataCenter/smartos-live) / [Homepage](https://www.TritonDataCenter.com/smartos))</small>
- Inclavare Containers <small> (&#9733; 536 / [Repository](https://github.com/inclavare-containers/inclavare-containers) / [Homepage](https://inclavare-containers.io/))</small>
- iSulad <small> (&#9733; 304 / [Repository](https://github.com/openeuler-mirror/iSulad) / [Homepage](https://gitee.com/openeuler/iSulad))</small>

### Runtime / Cloud Native Network
- Open vSwitch <small> (&#9733; 3,136 / [Repository](https://github.com/openvswitch/ovs) / [Homepage](https://www.openvswitch.org/))</small>
- FD.io <small> (&#9733; 945 / [Repository](https://github.com/FDio/vpp) / [Homepage](https://fd.io/))</small>

### Orchestration & Management / Service Proxy
- NGINX <small> (&#9733; 18,316 / [Repository](https://github.com/nginx/nginx) / [Homepage](https://www.nginx.com/))</small>
- Tengine <small> (&#9733; 11,985 / [Repository](https://github.com/alibaba/tengine) / [Homepage](https://tengine.taobao.org/))</small>
- OpenResty <small> (&#9733; 11,274 / [Repository](https://github.com/openresty/openresty) / [Homepage](https://openresty.com/en/))</small>
- HAProxy <small> (&#9733; 3,628 / [Repository](https://github.com/haproxy/haproxy) / [Homepage](https://www.haproxy.com/))</small>

### App Definition and Development / Database
- Redis <small> (&#9733; 59,524 / [Repository](https://github.com/redis/redis) / [Homepage](https://redis.io/))</small>
- TDengine <small> (&#9733; 21,184 / [Repository](https://github.com/taosdata/TDengine) / [Homepage](https://tdengine.com))</small>
- Timescale <small> (&#9733; 14,832 / [Repository](https://github.com/timescale/timescaledb) / [Homepage](https://www.timescale.com))</small>
- PostgreSQL <small> (&#9733; 12,235 / [Repository](https://github.com/postgres/postgres) / [Homepage](https://www.postgresql.org/))</small>
- YugabyteDB <small> (&#9733; 7,711 / [Repository](https://github.com/YugaByte/yugabyte-db) / [Homepage](https://www.yugabyte.com/yugabytedb/))</small>

### Observability and Analysis / Monitoring
- Netdata <small> (&#9733; 62,665 / [Repository](https://github.com/netdata/netdata) / [Homepage](https://www.netdata.cloud))</small>
- Nagios <small> (&#9733; 1,253 / [Repository](https://github.com/NagiosEnterprises/nagioscore) / [Homepage](https://www.nagios.com/))</small>

### Wasm / Runtime
- wasm3 <small> (&#9733; 6,020 / [Repository](https://github.com/wasm3/wasm3) / [Homepage](https://github.com/wasm3/wasm3))</small>
- wamr <small> (&#9733; 3,691 / [Repository](https://github.com/bytecodealliance/wasm-micro-runtime) / [Homepage](https://github.com/bytecodealliance/wasm-micro-runtime))</small>
- crunw <small> (&#9733; 26 / [Repository](https://github.com/second-state/crunw) / [Homepage](https://github.com/second-state/crunw))</small>

### Wasm / Toolchain
- emscripten <small> (&#9733; 23,634 / [Repository](https://github.com/emscripten-core/emscripten) / [Homepage](https://emscripten.org))</small>

## <span style="color:#89e051;">&#9679;</span> Shell <small>(18 projects)</small>

### Provisioning / Automation & Configuration
- Airship <small> (&#9733; 44 / [Repository](https://github.com/airshipit/treasuremap) / [Homepage](https://www.airshipit.org/))</small>

### Provisioning / Key Management
- SPIFFE <small> (&#9733; 1,213 / [Repository](https://github.com/spiffe/spiffe) / [Homepage](https://spiffe.io/))</small>

### Runtime / Cloud Native Storage
- Piraeus Datastore <small> (&#9733; 363 / [Repository](https://github.com/piraeusdatastore/piraeus) / [Homepage](https://piraeus.io/))</small>

### Runtime / Container Runtime
- Sysbox <small> (&#9733; 1,929 / [Repository](https://github.com/nestybox/sysbox) / [Homepage](https://github.com/nestybox/sysbox))</small>

### Orchestration & Management / Scheduling & Orchestration
- Open Cluster Management <small> (&#9733; 524 / [Repository](https://github.com/open-cluster-management-io/ocm) / [Homepage](https://open-cluster-management.io/))</small>

### App Definition and Development / Database
- KubeDB by AppsCode <small> (&#9733; 519 / [Repository](https://github.com/kubedb/operator) / [Homepage](https://kubedb.com))</small>

### App Definition and Development / Streaming & Messaging
- CDEvents <small> (&#9733; 71 / [Repository](https://github.com/cdevents/spec) / [Homepage](https://cdevents.dev))</small>

### App Definition and Development / Application Definition & Image Build
- Open Service Broker API <small> (&#9733; 1,142 / [Repository](https://github.com/openservicebrokerapi/servicebroker) / [Homepage](https://www.openservicebrokerapi.org/))</small>

### App Definition and Development / Continuous Integration & Delivery
- Spinnaker <small> (&#9733; 8,877 / [Repository](https://github.com/spinnaker/spinnaker) / [Homepage](https://www.spinnaker.io/))</small>
- Razee <small> (&#9733; 415 / [Repository](https://github.com/razee-io/Razee) / [Homepage](https://razee.io/))</small>

### Platform / Certified Kubernetes - Distribution
- Amazon Elastic Kubernetes Service Distro (Amazon EKS-D) <small> (&#9733; 1,239 / [Repository](https://github.com/aws/eks-distro) / [Homepage](https://aws.amazon.com/eks/eks-distro))</small>
- kURL <small> (&#9733; 656 / [Repository](https://github.com/replicatedhq/kurl) / [Homepage](https://kurl.sh))</small>
- AlviStack Ansible Collection for Kubernetes <small> (&#9733; 36 / [Repository](https://github.com/alvistack/ansible-collection-kubernetes) / [Homepage](https://github.com/alvistack/ansible-collection-kubernetes))</small>
- Elastisys Compliant Kubernetes <small> (&#9733; 33 / [Repository](https://github.com/elastisys/compliantkubernetes-apps) / [Homepage](https://elastisys.io/compliantkubernetes))</small>
- Desktop Kubernetes <small> (&#9733; 10 / [Repository](https://github.com/aceeric/desktop-kubernetes) / [Homepage](https://github.com/aceeric/desktop-kubernetes))</small>
- Magellano <small> (&#9733; 5 / [Repository](https://github.com/mia-platform/distribution) / [Homepage](https://mia-platform.eu/))</small>
- QBO <small> (&#9733; 4 / [Repository](https://github.com/alexeadem/qbo-home) / [Homepage](https://github.com/alexeadem/qbo-home))</small>

### Platform / Certified Kubernetes - Hosted
- KubeSphere®️ (QKE) <small> (&#9733; 27 / [Repository](https://github.com/QingCloudAppcenter/QKE) / [Homepage](https://www.qingcloud.com/products/kubesphereqke/))</small>

## <span style="color:#2b7489;">&#9679;</span> TypeScript <small>(18 projects)</small>

### App Definition and Development / Streaming & Messaging
- deepstream <small> (&#9733; 7,071 / [Repository](https://github.com/deepstreamIO/deepstream.io) / [Homepage](https://deepstream.io/))</small>

### App Definition and Development / Application Definition & Image Build
- Backstage <small> (&#9733; 21,542 / [Repository](https://github.com/backstage/backstage) / [Homepage](https://backstage.io/))</small>
- Eclipse Che <small> (&#9733; 6,805 / [Repository](https://github.com/eclipse/che) / [Homepage](https://www.eclipse.org/che/))</small>
- Kui <small> (&#9733; 2,498 / [Repository](https://github.com/kubernetes-sigs/kui) / [Homepage](https://kui.tools/))</small>
- Artifact Hub <small> (&#9733; 1,224 / [Repository](https://github.com/artifacthub/hub) / [Homepage](https://artifacthub.io/))</small>
- Monokle <small> (&#9733; 1,130 / [Repository](https://github.com/kubeshop/monokle) / [Homepage](https://monokle.kubeshop.io))</small>
- Plural <small> (&#9733; 1,071 / [Repository](https://github.com/pluralsh/plural) / [Homepage](https://www.plural.sh/))</small>
- Lagoon <small> (&#9733; 475 / [Repository](https://github.com/uselagoon/lagoon) / [Homepage](https://github.com/uselagoon/lagoon))</small>

### Platform / PaaS/Container Service
- JHipster <small> (&#9733; 20,495 / [Repository](https://github.com/jhipster/generator-jhipster) / [Homepage](https://www.jhipster.tech/))</small>
- Kubero <small> (&#9733; 608 / [Repository](https://github.com/kubero-dev/kubero) / [Homepage](https://www.kubero.dev/))</small>

### Serverless / Tools
- Hasura GraphQL Engine <small> (&#9733; 29,606 / [Repository](https://github.com/hasura/graphql-engine) / [Homepage](https://hasura.io/event-triggers))</small>
- Serverless Devs <small> (&#9733; 1,456 / [Repository](https://github.com/serverless-devs/serverless-devs) / [Homepage](https://www.serverless-devs.com/))</small>

### Serverless / Framework
- Midway Serverless <small> (&#9733; 6,564 / [Repository](https://github.com/midwayjs/midway) / [Homepage](https://github.com/midwayjs/midway))</small>
- Webiny <small> (&#9733; 6,514 / [Repository](https://github.com/webiny/webiny-js) / [Homepage](https://www.webiny.com))</small>

### Observability and Analysis / Monitoring
- Grafana <small> (&#9733; 54,952 / [Repository](https://github.com/grafana/grafana) / [Homepage](https://grafana.com/))</small>
- Opstrace <small> (&#9733; 1,212 / [Repository](https://github.com/opstrace/opstrace) / [Homepage](https://www.opstrace.com/))</small>

### Wasm / Toolchain
- WaPC <small> (&#9733; 26 / [Repository](https://github.com/wapc/wapc-js) / [Homepage](https://wapc.io/))</small>

### Wasm / Installable Platform
- hippo <small> (&#9733; 372 / [Repository](https://github.com/deislabs/hippo) / [Homepage](https://docs.hippofactory.dev))</small>

## <span style="color:#f1e05a;">&#9679;</span> JavaScript <small>(16 projects)</small>

### Runtime / Cloud Native Storage
- Zenko <small> (&#9733; 476 / [Repository](https://github.com/scality/zenko) / [Homepage](https://www.zenko.io))</small>

### Orchestration & Management / Scheduling & Orchestration
- OpenNebula <small> (&#9733; 976 / [Repository](https://github.com/OpenNebula/one) / [Homepage](https://opennebula.io/))</small>

### App Definition and Development / Application Definition & Image Build
- OpenAPI <small> (&#9733; 26,266 / [Repository](https://github.com/OAI/OpenAPI-Specification) / [Homepage](https://www.openapis.org/))</small>

### App Definition and Development / Continuous Integration & Delivery
- Screwdriver <small> (&#9733; 969 / [Repository](https://github.com/screwdriver-cd/screwdriver) / [Homepage](https://screwdriver.cd))</small>
- Travis CI <small> (&#9733; 608 / [Repository](https://github.com/travis-ci/travis-web) / [Homepage](https://travis-ci.com/))</small>
- Ortelius <small> (&#9733; 272 / [Repository](https://github.com/ortelius/ortelius) / [Homepage](https://ortelius.io/))</small>
- OpenFeature <small> (&#9733; 76 / [Repository](https://github.com/open-feature/community) / [Homepage](https://openfeature.dev/))</small>

### Serverless / Tools
- Node Lambda <small> (&#9733; 1,315 / [Repository](https://github.com/motdotla/node-lambda) / [Homepage](https://github.com/motdotla/node-lambda))</small>
- Cloud Native Landscape <small> (&#9733; 218 / [Repository](https://github.com/cncf/landscapeapp) / [Homepage](https://landscape.cncf.io/))</small>

### Serverless / Framework
- Serverless <small> (&#9733; 44,581 / [Repository](https://github.com/serverless/serverless) / [Homepage](https://serverless.com/))</small>
- SST <small> (&#9733; 13,720 / [Repository](https://github.com/serverless-stack/sst) / [Homepage](https://sst.dev/))</small>
- Sparta <small> (&#9733; 720 / [Repository](https://github.com/mweagle/Sparta) / [Homepage](https://gosparta.io/))</small>
- Architect <small> (&#9733; 155 / [Repository](https://github.com/architect/functions) / [Homepage](https://arc.codes/docs/en/get-started/quickstart))</small>

### Serverless / Installable Platform
- Knix <small> (&#9733; 185 / [Repository](https://github.com/knix-microfunctions/knix) / [Homepage](https://knix.io/))</small>

### Observability and Analysis / Monitoring
- Graphite <small> (&#9733; 5,648 / [Repository](https://github.com/graphite-project/graphite-web) / [Homepage](https://graphiteapp.org/))</small>
- Skooner <small> (&#9733; 1,092 / [Repository](https://github.com/skooner-k8s/skooner) / [Homepage](https://skooner.io/))</small>

## <span style="color:#701516;">&#9679;</span> Ruby <small>(11 projects)</small>

### Provisioning / Automation & Configuration
- Chef Infra <small> (&#9733; 7,191 / [Repository](https://github.com/chef/chef) / [Homepage](https://www.chef.io/))</small>
- Puppet <small> (&#9733; 6,905 / [Repository](https://github.com/puppetlabs/puppet) / [Homepage](https://puppet.com/))</small>
- Foreman <small> (&#9733; 2,329 / [Repository](https://github.com/theforeman/foreman) / [Homepage](https://theforeman.org/))</small>
- BOSH <small> (&#9733; 2,003 / [Repository](https://github.com/cloudfoundry/bosh) / [Homepage](https://bosh.io/docs/))</small>
- ManageIQ <small> (&#9733; 1,266 / [Repository](https://github.com/ManageIQ/manageiq) / [Homepage](https://www.manageiq.org/))</small>

### Provisioning / Container Registry
- Portus <small> (&#9733; 2,991 / [Repository](https://github.com/SUSE/Portus) / [Homepage](http://port.us.org/))</small>

### Provisioning / Security & Compliance
- Chef InSpec <small> (&#9733; 2,657 / [Repository](https://github.com/inspec/inspec) / [Homepage](https://community.chef.io/tools/chef-inspec))</small>

### Provisioning / Key Management
- CyberArk Conjur <small> (&#9733; 634 / [Repository](https://github.com/cyberark/conjur) / [Homepage](https://www.conjur.org))</small>

### App Definition and Development / Continuous Integration & Delivery
- GitLab <small> (&#9733; 23,222 / [Repository](https://github.com/gitlabhq/gitlabhq) / [Homepage](https://about.gitlab.com/))</small>

### Platform / Certified Kubernetes - Installer
- puppetlabs-kubernetes <small> (&#9733; 88 / [Repository](https://github.com/puppetlabs/puppetlabs-kubernetes) / [Homepage](https://forge.puppet.com/modules/puppetlabs/kubernetes))</small>

### Observability and Analysis / Logging
- Fluentd <small> (&#9733; 11,914 / [Repository](https://github.com/fluent/fluentd) / [Homepage](https://www.fluentd.org/))</small>

## <span style="color:#427819;">&#9679;</span> Makefile <small>(6 projects)</small>

### Runtime / Cloud Native Storage
- Container Storage Interface (CSI) <small> (&#9733; 1,159 / [Repository](https://github.com/container-storage-interface/spec) / [Homepage](https://github.com/container-storage-interface))</small>
- Triton Object Storage <small> (&#9733; 585 / [Repository](https://github.com/TritonDataCenter/manta) / [Homepage](https://www.tritondatacenter.com/triton/object-storage))</small>

### Orchestration & Management / Service Mesh
- Service Mesh Interface (SMI) <small> (&#9733; 1,022 / [Repository](https://github.com/servicemeshinterface/smi-spec) / [Homepage](https://smi-spec.io))</small>
- OpenSergo <small> (&#9733; 595 / [Repository](https://github.com/opensergo/opensergo-specification) / [Homepage](https://opensergo.io/))</small>
- Service Mesh Performance <small> (&#9733; 239 / [Repository](https://github.com/service-mesh-performance/service-mesh-performance) / [Homepage](https://smp-spec.io/))</small>

### App Definition and Development / Application Definition & Image Build
- Serverless Workflow <small> (&#9733; 572 / [Repository](https://github.com/serverlessworkflow/specification) / [Homepage](https://serverlessworkflow.github.io))</small>

## <span style="color:#000080;">&#9679;</span> Lua <small>(6 projects)</small>

### Orchestration & Management / API Gateway
- Kong <small> (&#9733; 34,641 / [Repository](https://github.com/Kong/kong) / [Homepage](https://konghq.com/))</small>
- APISIX <small> (&#9733; 11,679 / [Repository](https://github.com/apache/apisix) / [Homepage](https://apisix.apache.org/))</small>
- APIOAK <small> (&#9733; 399 / [Repository](https://github.com/apioak/apioak) / [Homepage](https://apioak.com/))</small>
- 3Scale <small> (&#9733; 283 / [Repository](https://github.com/3scale/apicast) / [Homepage](https://www.3scale.net/))</small>

### App Definition and Development / Database
- Tarantool <small> (&#9733; 3,151 / [Repository](https://github.com/tarantool/tarantool) / [Homepage](https://www.tarantool.io/en/))</small>

### Observability and Analysis / Monitoring
- sysdig <small> (&#9733; 7,226 / [Repository](https://github.com/draios/sysdig) / [Homepage](https://sysdig.com/opensource/))</small>

## <span style="color:#c22d40;">&#9679;</span> Scala <small>(5 projects)</small>

### Provisioning / Security & Compliance
- Rudder <small> (&#9733; 428 / [Repository](https://github.com/normation/rudder) / [Homepage](https://www.rudder.io/))</small>

### App Definition and Development / Database
- Apache CarbonData <small> (&#9733; 1,362 / [Repository](https://github.com/apache/carbondata) / [Homepage](https://carbondata.apache.org/))</small>

### App Definition and Development / Streaming & Messaging
- Apache Spark <small> (&#9733; 35,545 / [Repository](https://github.com/apache/spark) / [Homepage](https://spark.apache.org/))</small>

### Platform / PaaS/Container Service
- Akka <small> (&#9733; 12,673 / [Repository](https://github.com/akka/akka) / [Homepage](https://akka.io/))</small>

### Serverless / Installable Platform
- Apache OpenWhisk <small> (&#9733; 6,028 / [Repository](https://github.com/apache/openwhisk) / [Homepage](https://openwhisk.apache.org/))</small>

## <span style="color:inherit;">&#9679;</span> Jinja <small>(5 projects)</small>

### App Definition and Development / Application Definition & Image Build
- Konveyor <small> (&#9733; 13 / [Repository](https://github.com/konveyor/tackle2-operator) / [Homepage](https://www.konveyor.io/))</small>

### Platform / Certified Kubernetes - Distribution
- AgoraKube <small> (&#9733; 89 / [Repository](https://github.com/ilkilab/agorakube) / [Homepage](https://github.com/ilkilab/agorakube))</small>

### Platform / Certified Kubernetes - Installer
- Kubespray <small> (&#9733; 13,797 / [Repository](https://github.com/kubernetes-sigs/kubespray) / [Homepage](https://kubespray.io/))</small>
- Kubeasz <small> (&#9733; 9,037 / [Repository](https://github.com/easzlab/kubeasz) / [Homepage](https://github.com/easzlab/kubeasz))</small>
- AlviStack Vagrant Box Packaging for Kubernetes <small> (&#9733; 14 / [Repository](https://github.com/alvistack/vagrant-kubernetes) / [Homepage](https://github.com/alvistack/vagrant-kubernetes))</small>

## <span style="color:#e69f56;">&#9679;</span> Groovy <small>(2 projects)</small>

### Provisioning / Automation & Configuration
- Rundeck <small> (&#9733; 4,919 / [Repository](https://github.com/rundeck/rundeck) / [Homepage](https://www.rundeck.com/open-source))</small>

### App Definition and Development / Application Definition & Image Build
- Gradle Build Tool <small> (&#9733; 14,590 / [Repository](https://github.com/gradle/gradle) / [Homepage](https://gradle.org))</small>

## <span style="color:inherit;">&#9679;</span> Mustache <small>(2 projects)</small>

### Orchestration & Management / Service Proxy
- Inlets <small> (&#9733; 475 / [Repository](https://github.com/inlets/inlets-pro) / [Homepage](https://docs.inlets.dev))</small>

### Platform / PaaS/Container Service
- Otomi <small> (&#9733; 1,621 / [Repository](https://github.com/redkubes/otomi-core) / [Homepage](https://otomi.io))</small>

## <span style="color:#178600;">&#9679;</span> C# <small>(2 projects)</small>

### Serverless / Hosted Platform
- Azure Functions <small> (&#9733; 1,823 / [Repository](https://github.com/Azure/azure-functions-host) / [Homepage](https://azure.microsoft.com/en-us/services/functions/))</small>

### Observability and Analysis / Tracing
- OpenTelemetry <small> (&#9733; 607 / [Repository](https://github.com/open-telemetry/community) / [Homepage](https://opentelemetry.io/))</small>

## <span style="color:#4F5D95;">&#9679;</span> PHP <small>(2 projects)</small>

### Observability and Analysis / Monitoring
- Zabbix <small> (&#9733; 2,942 / [Repository](https://github.com/zabbix/zabbix) / [Homepage](https://www.zabbix.com/))</small>
- Centreon <small> (&#9733; 30 / [Repository](https://github.com/centreon/centreon) / [Homepage](https://www.centreon.com/))</small>

## <span style="color:#5e5086;">&#9679;</span> Haskell <small>(1 project)</small>

### Provisioning / Security & Compliance
- FOSSA <small> (&#9733; 1,099 / [Repository](https://github.com/fossas/fossa-cli) / [Homepage](https://fossa.com/))</small>

## <span style="color:inherit;">&#9679;</span> Open Policy Agent <small>(1 project)</small>

### Provisioning / Security & Compliance
- KICS <small> (&#9733; 1,526 / [Repository](https://github.com/Checkmarx/kics) / [Homepage](https://kics.io/))</small>

## <span style="color:#EB8CEB;">&#9679;</span> XSLT <small>(1 project)</small>

### Provisioning / Security & Compliance
- OpenSCAP <small> (&#9733; 1,090 / [Repository](https://github.com/OpenSCAP/openscap) / [Homepage](https://www.open-scap.org/))</small>

## <span style="color:#6e4a7e;">&#9679;</span> Elixir <small>(1 project)</small>

### Orchestration & Management / API Gateway
- Reactive Interaction Gateway <small> (&#9733; 557 / [Repository](https://github.com/accenture/reactive-interaction-gateway) / [Homepage](https://accenture.github.io/reactive-interaction-gateway/))</small>

## <span style="color:#db5855;">&#9679;</span> Clojure <small>(1 project)</small>

### App Definition and Development / Database
- Crux <small> (&#9733; 2,196 / [Repository](https://github.com/xtdb/xtdb) / [Homepage](https://xtdb.com/index.html))</small>

## <span style="color:#B83998;">&#9679;</span> Erlang <small>(1 project)</small>

### App Definition and Development / Streaming & Messaging
- EMQ Technologies <small> (&#9733; 11,479 / [Repository](https://github.com/emqx/emqx) / [Homepage](https://www.emqx.io/))</small>

## <span style="color:inherit;">&#9679;</span> Starlark <small>(1 project)</small>

### App Definition and Development / Streaming & Messaging
- RabbitMQ <small> (&#9733; 10,592 / [Repository](https://github.com/rabbitmq/rabbitmq-server) / [Homepage](https://www.rabbitmq.com/))</small>

## <span style="color:inherit;">&#9679;</span> Smarty <small>(1 project)</small>

### Platform / Certified Kubernetes - Distribution
- Fury Distribution <small> (&#9733; 110 / [Repository](https://github.com/sighupio/fury-distribution) / [Homepage](https://sighup.io))</small>

## <span style="color:#646464;">&#9679;</span> SaltStack <small>(1 project)</small>

### Platform / Certified Kubernetes - Distribution
- MetalK8s <small> (&#9733; 318 / [Repository](https://github.com/scality/metalk8s) / [Homepage](https://www.zenko.io/metalk8s/))</small>

## <span style="color:inherit;">&#9679;</span> HCL <small>(1 project)</small>

### Platform / Certified Kubernetes - Distribution
- Typhoon <small> (&#9733; 1,798 / [Repository](https://github.com/poseidon/typhoon) / [Homepage](https://typhoon.psdn.io/))</small>

## <span style="color:#384d54;">&#9679;</span> Dockerfile <small>(1 project)</small>

### Platform / PaaS/Container Service
- No Code <small> (&#9733; 56,473 / [Repository](https://github.com/kelseyhightower/nocode) / [Homepage](https://github.com/kelseyhightower/nocode))</small>

## <span style="color:#563d7c;">&#9679;</span> CSS <small>(1 project)</small>

### Serverless / Framework
- Flogo <small> (&#9733; 2,240 / [Repository](https://github.com/TIBCOSoftware/flogo) / [Homepage](https://www.flogo.io))</small>

## <span style="color:#0064bd;">&#9679;</span> Jsonnet <small>(1 project)</small>

### Serverless / Installable Platform
- PipelineAI <small> (&#9733; 4,158 / [Repository](https://github.com/pipelineai/pipeline) / [Homepage](https://www.datascienceonaws.com))</small>

## <span style="color:#e34c26;">&#9679;</span> HTML <small>(1 project)</small>

### Observability and Analysis / Chaos Engineering
- Litmus <small> (&#9733; 3,588 / [Repository](https://github.com/litmuschaos/litmus) / [Homepage](https://litmuschaos.io/))</small>

## <span style="color:#04133b;">&#9679;</span> WebAssembly <small>(1 project)</small>

### Wasm / Specifications
- Wasm <small> (&#9733; 2,876 / [Repository](https://github.com/WebAssembly/spec) / [Homepage](https://webassembly.org))</small>