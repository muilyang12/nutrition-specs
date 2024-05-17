import { axiosInstance } from "./axiosInstance";

export const foodApi = {
  getFoodCategories: async () => (await axiosInstance.get("/food/food-category")).data,
  getProducts: async (foodCategoryId: number) =>
    (await axiosInstance.get(`/food/product?food-category=${foodCategoryId}`)).data,
  getNutritions: async (productId: number) =>
    (await axiosInstance.get(`/food/nutrition?product=${productId}`)).data,
};
