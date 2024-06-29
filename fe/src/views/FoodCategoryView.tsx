import FoodCategorySelect from "@components/FoodCategorySelect";
import BrandFilter from "@components/brand-filter/BrandFilter.server";
import ProductList from "@components/product-list/ProductList.server";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default function FoodCategoryView(props: Props) {
  const { selectedFoodCategoryKey } = props;

  return (
    <>
      <FoodCategorySelect />

      <BrandFilter selectedFoodCategoryKey={selectedFoodCategoryKey} />

      <ProductList selectedFoodCategoryKey={selectedFoodCategoryKey} />
    </>
  );
}
