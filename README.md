# JWT Authentication with Vercel and Python for Ghost Admin API

> This is an example of how to authenticate with the Ghost administration API using JWT with Vercel and Python.

Requirements

* A Vercel account
* A Ghost project
* Python 3.9+

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

Send a request with:
```http

POST http://localhost:3000/create HTTP/1.1
content-type: application/json

{
    "private_key": "your_admin_API_key"
}

```

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask&demo-title=Flask%20%2B%20Vercel&demo-description=Use%20Flask%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
