# HTTP Status Code Explanations

This document provides explanations for common HTTP status codes used in web development. Understanding these codes is crucial for building robust and reliable web applications.

## Status Code Ranges

HTTP status codes are grouped into five ranges, each indicating a different type of response:

* **1xx (Informational):** The request was received, and the server is continuing the process.
* **2xx (Success):** The request was successfully received, understood, and accepted.
* **3xx (Redirection):** Further action is required by the client to complete the request.
* **4xx (Client Errors):** The client made an error in the request.
* **5xx (Server Errors):** The server encountered an error while processing the request.

## Common Status Codes

Here's a breakdown of some of the most frequently encountered status codes:

### 2xx Success

* **200 OK:**
    * Indicates that the request was successful.
    * This is the standard response for successful HTTP requests.
* **201 Created:**
    * Indicates that the request resulted in the creation of a new resource.
    * Commonly used after a successful `POST` request.
* **204 No Content:**
    * Indicates that the server successfully processed the request, but there is no content to send back.
    * Often used after a successful `DELETE` request.

### 3xx Redirection

* **301 Moved Permanently:**
    * Indicates that the requested resource has been permanently moved to a new URL.
    * Clients should update their bookmarks and links.
* **302 Found (or 307 Temporary Redirect):**
    * Indicates that the requested resource has been temporarily moved to a new URL.
    * Clients should use the new URL for this request, but continue to use the old URL for future requests.
* **304 Not Modified:**
    * Indicates that the client's cached version of the resource is still valid.
    * Saves bandwidth by preventing the server from sending the same data again.

### 4xx Client Errors

* **400 Bad Request:**
    * Indicates that the server cannot understand the request due to invalid syntax.
    * Often occurs when the client sends malformed data.
* **401 Unauthorized:**
    * Indicates that the client must authenticate to access the requested resource.
    * The client needs to provide valid credentials.
* **403 Forbidden:**
    * Indicates that the client does not have permission to access the requested resource.
    * Even with valid credentials, access is denied.
* **404 Not Found:**
    * Indicates that the requested resource could not be found on the server.
    * The URL may be incorrect, or the resource may have been deleted.
* **405 Method Not Allowed:**
    * Indicates that the request method (GET, POST, etc.) is not allowed for the requested resource.
* **409 Conflict:**
    * Indicates that the request could not be completed due to a conflict with the current state of the resource.

### 5xx Server Errors

* **500 Internal Server Error:**
    * Indicates that a generic error occurred on the server.
    * This is a catch-all error for unexpected server-side issues.
* **501 Not Implemented:**
    * Indicates that the server does not support the functionality required to fulfill the request.
* **503 Service Unavailable:**
    * Indicates that the server is temporarily unavailable (e.g., due to maintenance or overload).

## Importance

Using the correct status codes is essential for:

* Providing clear communication between clients and servers.
* Enabling proper error handling in client-side applications.
* Improving SEO by allowing search engines to understand the status of web pages.
* Facilitating debugging and troubleshooting.
* Creating well designed and predictable APIs.