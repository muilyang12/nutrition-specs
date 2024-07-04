import { create } from "zustand";

interface CompareStore {
  isComparing: boolean;
  toggleIsComparing: () => void;
}

export const useCompareStore = create<CompareStore>()((set) => ({
  isComparing: false,
  toggleIsComparing: () => set((state) => ({ isComparing: !state.isComparing })),
}));
