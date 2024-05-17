import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import { useFoodCategoriesStore } from "../stores/useFoodCategories";
import { foodApi } from "../apis/food";

export default function ProductList() {
  const [searchParams] = useSearchParams();

  const { foodCategories } = useFoodCategoriesStore();

  const [products, setProducts] = useState([]);

  useEffect(() => {
    if (searchParams.size === 0 || foodCategories.length === 0) return;

    setProducts([]);

    const categoryId = foodCategories.find(
      (category) => category.category_name === searchParams.get("food-category")
    )?.id;

    if (!categoryId) return;

    foodApi.getProducts(categoryId).then((data) => setProducts(data.products));
  }, [searchParams, foodCategories]);

  if (searchParams.size === 0 || foodCategories.length === 0)
    return <>음식 카테고리를 선택해주세요.</>;
  else
    return (
      <>
        {products.map((product) => (
          <Accordion key={`${product.brand_name} - ${product.product_name}`}>
            <AccordionSummary
              aria-controls="panel1-content"
              id={`${product.brand_name} - ${product.product_name}`}
            >
              {`${product.brand_name} - ${product.product_name}`}
            </AccordionSummary>
            <AccordionDetails>{`${product.brand_name} - ${product.product_name}`}</AccordionDetails>
          </Accordion>
        ))}
      </>
    );
}
