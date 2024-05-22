"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import { useFoodCategoriesStore } from "@stores/useFoodCategories";
import { FoodCategoryPageParams } from "@defines/params.define";
import ProductDetail from "./ProductDetail";
import { ProductRs } from "@apis/food.define";
import { foodApi } from "@apis/food";

export default function ProductList() {
  const params = useParams<FoodCategoryPageParams>();
  const selectedFoodCategoryKey = params.foodCategory;

  const { foodCategories } = useFoodCategoriesStore();

  const [products, setProducts] = useState<ProductRs[]>([]);

  useEffect(() => {
    if (!selectedFoodCategoryKey || foodCategories.length === 0) return;

    setProducts([]);

    const categoryId = foodCategories.find(
      (category) => category.category_key === selectedFoodCategoryKey
    )?.id;

    if (!categoryId) return;

    foodApi.getProducts(categoryId).then((data) => setProducts(data));
  }, [params, foodCategories]);

  if (!selectedFoodCategoryKey || foodCategories.length === 0)
    return <>음식 카테고리를 선택해주세요.</>;

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
          <AccordionDetails>
            <ProductDetail productId={product.id} />
          </AccordionDetails>
        </Accordion>
      ))}
    </>
  );
}
