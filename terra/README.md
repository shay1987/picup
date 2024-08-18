# Terraform files

## main.tf

The `main.tf` file follows its name:  
It is the manifest that holds all the instructions to create the environment and resources you want/need.  

## provider.tf
The `provider.tf` file allows Terraform to interact with the cloud provider, depends on the provider and the call.  

## output.tf
The `output.tf` file provide information about your infrastructure available on the command line, and can expose information for other Terraform configurations to use.  

## variable.tf
The `variable.tf` file holds all the variables for the other Terraform files and it is used like this:  
```
<variable = var.name>
```
