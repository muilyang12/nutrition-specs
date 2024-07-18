import { create } from "zustand";

interface BrandFilterStore {
  selectedFilters: string[];
  setSelectedFilters: (newFilters: string[]) => void;
  addSelectedFilter: (newFilter: string) => void;
  deleteSelectedFilter: (targetFilter: string) => void;
}

export const useBrandFilterStore = create<BrandFilterStore>()((set) => ({
  selectedFilters: [],
  setSelectedFilters: (newFilters: string[]) => set(() => ({ selectedFilters: newFilters })),
  addSelectedFilter: (newFilter: string) =>
    set((prev) => ({ selectedFilters: [...prev.selectedFilters, newFilter] })),
  deleteSelectedFilter: (targetFilter: string) =>
    set((prev) => ({
      selectedFilters: prev.selectedFilters.filter((brandName) => brandName !== targetFilter),
    })),
}));
