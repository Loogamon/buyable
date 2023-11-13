function goto_product(id)
{
	window.location.href = "/item/view?id="+id;
}

function cart_delete(id)
{
	window.location.href = "/mycart?action=delete&id="+id;
}

function cart_clear()
{
	window.location.href = "/mycart?action=clear";
}