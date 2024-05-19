import { create } from "zustand";
import { FoodCategoryRs } from "../apis/food.define";

interface FoodCategories extends FoodCategoryRs {
  label: string;
}

interface FoodCategoriesStore {
  foodCategories: FoodCategories[];
  setFoodCategories: (newFoodCategories: FoodCategories[]) => void;
}

export const useFoodCategoriesStore = create<FoodCategoriesStore>((set) => ({
  foodCategories: [],
  setFoodCategories: (newFoodCategories: FoodCategories[]) =>
    set({ foodCategories: newFoodCategories }),
}));
