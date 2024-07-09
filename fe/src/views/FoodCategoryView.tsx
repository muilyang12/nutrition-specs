import { Suspense } from "react";
import LayoutHeader from "@components/layout-header/LayoutHeader";
import CategoryMenu from "@components/category-menu/CategoryMenu.server";
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

        <CategoryMenu selectedFoodCategoryKey={selectedFoodCategoryKey} />

        <Suspense>
          <BrandFilter selectedFoodCategoryKey={selectedFoodCategoryKey} />
        </Suspense>
      </header>

      <ProductList selectedFoodCategoryKey={selectedFoodCategoryKey} />

      <CompareButton />
    </>
  );
}
