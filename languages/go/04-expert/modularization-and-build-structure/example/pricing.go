package main

type lineItem struct {
	name      string
	quantity  int
	unitPrice float64
}

type invoiceSummary struct {
	subtotal      float64
	discountValue float64
	taxValue      float64
	total         float64
}

func buildSummary(items []lineItem, discountPercent, taxPercent float64) invoiceSummary {
	subtotal := 0.0
	for _, item := range items {
		subtotal += float64(item.quantity) * item.unitPrice
	}

	discountValue := subtotal * (discountPercent / 100.0)
	taxedBase := subtotal - discountValue
	taxValue := taxedBase * (taxPercent / 100.0)

	return invoiceSummary{
		subtotal:      subtotal,
		discountValue: discountValue,
		taxValue:      taxValue,
		total:         taxedBase + taxValue,
	}
}
