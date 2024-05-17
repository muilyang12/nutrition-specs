import { create } from "zustand";

export const useFoodCategoriesStore = create((set) => ({
  foodCategories: [],
  setFoodCategories: (newFoodCategories) => set({ foodCategories: newFoodCategories }),
}));
