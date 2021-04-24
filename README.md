# Docs API
API to manage DOCX templates and generate documents based on them

[![Build and Deploy](https://github.com/jetervaz/docsapi/actions/workflows/build_deploy_dev.yml/badge.svg)](https://github.com/jetervaz/docsapi/actions/workflows/build_deploy_dev.yml)

## Development

- Python 3.6
- NPM

Install development requirements:
```
npm install -g serverless
npm install -g serverless-prune-plugin
npm install -g serverless-python-requirements
```

Install python requirements:
```
pip install -r requirements.txt
```

Install python development requirements:
```
pip install -r requirements-dev.txt
```

## Deployment

To deploy the stack, run the following command:

```
serverless deploy --stage $DEPLOY_STAGE
```
