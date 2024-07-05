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
      <CategoryMenu selectedFoodCategoryKey={selectedFoodCategoryKey} />

      <BrandFilter selectedFoodCategoryKey={selectedFoodCategoryKey} />

      <ProductList selectedFoodCategoryKey={selectedFoodCategoryKey} />

      <CompareButton />
    </>
  );
}
