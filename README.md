# Picture application

## The application
The application is a simple [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) based [Python](https://www.python.org/) application that allows users to upload and manage images.  
<br />
The main parts for this are:  
### Main building blocks for the app

<a id="NGX"></a>

* **[NGINX](https://nginx.org/en/) Front end** that holds a [static website](https://en.wikipedia.org/wiki/Static_web_page) for login that is the gate to the application.   (Another option can be a secure login like [Keycloak](https://www.keycloak.org/))
* **[MySQL](https://www.mysql.com/) Databse** to hold the users login credentials.  
* **The Application** based on [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)).  
* **[GCP](https://console.cloud.google.com/) [Bucket](https://cloud.google.com/storage/docs/creating-buckets)** to hold the images.  
* **[GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)** is the platform that the application, as a whole, would run in.  
* **[GKE Ingress for Application Load Balancers](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress)** is a fully managed [LB](https://en.wikipedia.org/wiki/Load_balancing_(computing)) that will expose the [NGINX](#NGX) to the web.
* **GCP [Artifact Registry](https://cloud.google.com/artifact-registry/)** to store the application images.
* **[Github](https://github.com/)** for [version control](https://en.wikipedia.org/wiki/Distributed_version_control).
* **[Github actions](https://github.com/features/actions)** as a CI tool.
* **[Argo CD](https://argo-cd.readthedocs.io/en/stable/)** as a CD tool.
* **[Terraform](https://www.terraform.io/)** as a [IAC](https://en.wikipedia.org/wiki/Infrastructure_as_code).

