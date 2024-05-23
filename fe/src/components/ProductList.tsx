import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ProductDetail from "./ProductDetail";
import { NutritionRs, ProductRs } from "@apis/food.define";
import { foodApi } from "@apis/food";

interface Props {
  selectedFoodCategoryKey?: string;
}

export default async function ProductList(props: Props) {
  const { selectedFoodCategoryKey } = props;

  if (!selectedFoodCategoryKey) return <>음식 카테고리를 선택해주세요.</>;

  const products = await foodApi.getProducts(selectedFoodCategoryKey);
  const productIds = products.map((product) => product.id);
  const nutritions = await foodApi.getNutritions(productIds);
  const productsAndNutritions: [ProductRs, NutritionRs][] = products.map((product, index) => [
    product,
    nutritions[index],
  ]);

  return (
    <>
      {productsAndNutritions.map(([product, nutrition]) => (
        <Accordion key={`${product.brand_name} - ${product.product_name}`}>
          <AccordionSummary
            aria-controls="panel1-content"
            id={`${product.brand_name} - ${product.product_name}`}
          >
            {`${product.brand_name} - ${product.product_name}`}
          </AccordionSummary>
          <AccordionDetails>
            <ProductDetail nutrition={nutrition} />
          </AccordionDetails>
        </Accordion>
      ))}
    </>
  );
}
