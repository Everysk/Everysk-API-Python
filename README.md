<p align="center"><img src="https://www.everysk.com/images/everysk_logo.svg" width="400"></p>

# Everysk API

[Everysk](https://www.everysk.com/) API is organized around the open standard protocol [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. We use built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood by off-the-shelf HTTP clients. All API responses are returned in [JSON](https://www.json.org/json-en.html), including errors.

We also have some specific language examples to make integration easier. You can switch the programming language of the examples with the tabs in the top right. You can request a Trial API Key at [Contact Us](https://www.everysk.com/contact).
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Everysk API library:

```bash
pip install everysk
```
## Authentication

The API uses exclusive POST HTTP method to access resources URI. In the POST, you represent the arguments of methods in JSON encoded dictionary in the request body.

The maximum JSON encoded payload size is 1MB. Be sure to encode the following HTTP Content-Type header for your requests: "application/json".

Authenticate your account when using the API by including your secret API key in the request. Authentication to the API is performed via [HTTP Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). In short, you will use your Everysk API Account SID as the username and your Auth Token as the password for HTTP Basic authentication. API requests without authentication will fail. You can manage your API keys in the [API Settings](). Be sure to keep your Account SID and Auth Token secret.

The API is served over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP will fail.

**Important**. Make sure to replace **YOUR_ACCOUNT_SID** and **YOUR_AUTH_TOKEN** with your Account SID and your Auth Token.
### Risk Workflows for Developers

- Bottom-up and top-down granular risk attribution, factor modeling and stress testing using modern math finance.
- API includes calculations and data: no need to purchase separate data licenses.
- Benefit from a flexible REST API. Customize your ideal workflow in the language of your choice, performing calculations and controlling the platform.

## Support

Visit our official website [https://everysk.com](https://www.everysk.com/) or reach out to the Everysk team at [contact@everysk.com](mailto:contact@everysk.com).

## Announcements

Follow [@everysktech](https://twitter.com/everysktech) on Twitter for announcements and updates about this library.
