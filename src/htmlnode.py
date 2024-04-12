class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[object] = None,
        props: dict = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = f""
        if self.props:
            for prop in list(self.props):
                html += f' {prop}="{self.props[prop]}"'
        else:
            return ""
        return html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value: str, props: dict = None, tag: str = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: No value")
        elif self.tag is None:
            return self.value
        elif self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[object], props: dict = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):        
        if self.tag is None:
            raise ValueError("Invalid Html: No tag")
        elif self.children is None:
            raise ValueError("No Children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
