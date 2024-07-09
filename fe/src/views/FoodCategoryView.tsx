import { Suspense } from "react";
import LayoutHeader from "@components/layout-header/LayoutHeader";
import MainCategoryMenu from "@components/main-category-menu/MainCategoryMenu.server";
import BrandFilter from "@components/brand-filter/BrandFilter.server";
import ProductList from "@components/product-list/ProductList.server";
import CompareButton from "@components/compare-button/CompareButton";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default function FoodCategoryView(props: Props) {
  const { selectedFoodCategoryKey } = props;

  return (
    <>
      <header>
        <LayoutHeader />

        <MainCategoryMenu selectedFoodCategoryKey={selectedFoodCategoryKey} />

        <Suspense>
          <BrandFilter selectedFoodCategoryKey={selectedFoodCategoryKey} />
        </Suspense>
      </header>

      <ProductList selectedFoodCategoryKey={selectedFoodCategoryKey} />

      <CompareButton />
    </>
  );
}
