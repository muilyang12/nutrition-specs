import axios from "axios";

const isProd = process.env.NODE_ENV == "production";

export const axiosInstance = axios.create({
  baseURL: isProd ? "https://api.nutrition-specs.com/" : "http://127.0.0.1:8000/",
});
