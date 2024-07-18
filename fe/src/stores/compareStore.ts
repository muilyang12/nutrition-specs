import { create } from "zustand";

interface CompareStore {
  isComparing: boolean;
  toggleIsComparing: () => void;
  selectedProducts: number[];
  toggleSelectedProduct: (newProductId: number) => void;

  resetState: () => void;
}

const initialState = {
  isComparing: false,
  selectedProducts: [],
};

export const useCompareStore = create<CompareStore>()((set) => ({
  isComparing: false,
  toggleIsComparing: () => set((state) => ({ isComparing: !state.isComparing })),
  selectedProducts: [],
  toggleSelectedProduct: (newProductId: number) =>
    set((prev) => ({
      selectedProducts: prev.selectedProducts.includes(newProductId)
        ? prev.selectedProducts.filter((id) => id !== newProductId)
        : [...prev.selectedProducts, newProductId],
    })),
  resetState: () => set(initialState),
}));
