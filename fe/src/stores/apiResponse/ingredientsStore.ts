import { create } from "zustand";

interface IngredientsStore {
  ingredientRecord: Record<number, [string, string]>;
  addIngredientRecord: (
    ingredientId: number,
    ingredientName: string,
    ingredientExplanation: string
  ) => void;
}

export const useIngredientsStore = create<IngredientsStore>()((set) => ({
  ingredientRecord: {},
  addIngredientRecord: (
    ingredientId: number,
    ingredientName: string,
    ingredientExplanation: string
  ) =>
    set((prev) => ({
      ingredientRecord: {
        ...prev.ingredientRecord,
        [ingredientId]: [ingredientName, ingredientExplanation],
      },
    })),
}));
