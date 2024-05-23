import FoodCategorySelect from "@components/FoodCategorySelect";
import ProductList from "@components/ProductList";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default function FoodCategoryView(props: Props) {
  const { selectedFoodCategoryKey } = props;

  return (
    <>
      <FoodCategorySelect />
      <ProductList selectedFoodCategoryKey={selectedFoodCategoryKey} />
    </>
  );
}
