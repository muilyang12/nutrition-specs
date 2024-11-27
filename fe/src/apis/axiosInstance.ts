import axios from "axios";

const isBuilding = process.env.IS_BUILDING === "true";
const isProd = !isBuilding && process.env.NODE_ENV == "production";

export const axiosInstance = axios.create({
  baseURL: isProd ? "https://api.nutrition-specs.com/" : "http://127.0.0.1:8000/",
});
