# Install the package for AWS Secrets Manager
	`npm install @aws-sdk/client-secrets-manager`
[source]( https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-secrets-manager/index.html)

# Install CRACO to Override configuration of REACT app.
Due to creating the app via `Create React App` , React has set default webpack configuration. To run the code, we need to have the `top-level-await` configuration to be "true". Otherwise, we will get an error of "top-level-await not enabled". Therefore, we will leverage CRACO to modify the webpack in react.

Install [CRACO](https://github.com/dilanx/craco/blob/main/packages/craco/README.md#installation) to override configuration of REACT app. 

  `npm i -D @craco/craco`

# Created local environmnet for AWS Credential
Create a local enviroment file .env under ./frontend. Check slack channel #project-friendymap to find the credential.