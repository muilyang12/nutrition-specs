import { axiosInstance } from "./axiosInstance";
import { FoodCategoryRs, NutritionRs, ProductRs } from "./food.define";

export const foodApi = {
  getFoodCategories: async () =>
    (await axiosInstance.get<FoodCategoryRs[]>("food/food-category/")).data,
  getProducts: async (foodCategoryKey: string) =>
    (await axiosInstance.get<ProductRs[]>(`food/product/?category-key=${foodCategoryKey}`)).data,
  getNutritions: async (productIds: number[]) => {
    const queries = productIds.map((id) => `product=${id}`).join("&");

    return (await axiosInstance.get<NutritionRs[]>(`food/nutrition/?${queries}`)).data;
  },
};
