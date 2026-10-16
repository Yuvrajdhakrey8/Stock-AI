/**
 * DhakreyStock AI - Frontend Configuration
 * In local dev or AWS Amplify reverse-proxy mode, API_BASE_URL is empty string ('').
 * When calling an external AWS Lambda / API Gateway endpoint directly, define VITE_API_BASE_URL in environment.
 */
export const API_BASE_URL: string = (import.meta.env.VITE_API_BASE_URL || '').replace(/\/$/, '');
