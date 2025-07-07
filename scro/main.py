import random
from typing import Any, List, Tuple, Optional
from collections import namedtuple

QuantumElement = namedtuple('QuantumElement', ['value', 'weight'])

class SchrodingerStack:
    """
    A probabilistic stack where elements exist in superposition until observed.

    Inspired by quantum mechanics - elements have probability weights that determine
    their position in the stack only when the stack collapses (is observed).
    """
    def __init__(self) -> None:
        self._quantum_el: List[QuantumElement] = []
        self._collapsed_stack: Optional[List[Any]] = None
        self._is_collapsed = False

    def push(self, value: Any, weight: float = 1.0):
        """
        Push a value onto the stack with a given probability weight.

        Args:
            value: The value to push
            weight: Probability weight (higher = more likely to be on top)
        """
        if weight <= 0:
            raise ValueError("Weight must be positive")

        self._quantum_el.append(QuantumElement(value, weight))
        self._is_collapsed = False
        self._collapsed_stack = None

    def collapse(self) -> None:
        """
        Collapse the quantum superposition into a definite classical stack.
        Uses weighted random sampling to determine final order.
        """
        if self._is_collapsed or not self._quantum_el:
            pass

        remaining_el = self._quantum_el.copy()
        collapsed_order = []

        while remaining_el:
            total_w = sum(elem.weight for elem in remaining_el)
            rand_val = random.uniform(0, total_w)

            cum_w = 0
            selected_index = 0

            for idx, elem in enumerate(remaining_el):
                cum_w += elem.weight
                if rand_val <= cum_w:
                    selected_index = idx
                    break

            selected_element = remaining_el.pop(selected_index)
            collapsed_order.append(selected_element.value)

        self._collapsed_stack = list(reversed(collapsed_order))
        self._is_collapsed = True

    def pop(self) -> Any:
        """
        Collapse the stack if necessary, then pop and return the top element.

        Returns:
            The top element of the collapsed stack

        Raises:
            IndexError: If the stack is empty
        """
        if not self._quantum_el:
            raise IndexError("Popping empty stack")

        if not self._is_collapsed:
            self.collapse()

        popped_val = self._collapsed_stack.pop()

        for i, quantum_elem in enumerate(self._quantum_el):
            if quantum_elem.value == popped_val:
                self._quantum_el.pop(i)
                break

        if not self._quantum_el:
            self._is_collapsed = False
            self._collapsed_stack = None

        return popped_val

    def peek(self) -> Any:
        """
        Collapse the stack if necessary, then return (but don't remove) the top element.

        Returns:
            The top element of the collapsed stack

        Raises:
            IndexError: If the stack is empty
        """
        if not self._quantum_el:
            raise IndexError("peek from empty stack")

        if not self._is_collapsed:
            self.collapse()

        return self._collapsed_stack[-1]

    def reset(self) -> None:
        """
        Reset the stack to quantum superposition state.
        All elements return to uncertain positions.
        """
        self._is_collapsed = False
        self._collapsed_stack = None

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._quantum_el) == 0

    def size(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._quantum_el)

    def is_collapsed(self) -> bool:
        """Check if the stack is currently in collapsed state."""
        return self._is_collapsed

    def get_quantum_state(self) -> List[Tuple[Any, float]]:
        """
        Return the current quantum state (all elements with their weights).
        Useful for debugging or visualization.
        """
        return [(elem.value, elem.weight) for elem in self._quantum_el]

    def get_collapsed_state(self) -> Optional[List[Any]]:
        """
        Return the current collapsed state if available.
        Returns None if not collapsed.
        """
        return self._collapsed_stack.copy() if self._collapsed_stack else None

    def __str__(self) -> str:
        """String representation showing current state."""
        if self._is_collapsed:
            return f"SchrödingerStack(collapsed={self._collapsed_stack})"
        else:
            quantum_info = [(elem.value, elem.weight) for elem in self._quantum_el]
            return f"SchrödingerStack(quantum={quantum_info})"

    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":
    stack = SchrodingerStack()

    print("Pushing elements with weights:")
    stack.push("α", 1.0)
    stack.push("β", 3.0)
    stack.push("γ", 2.0)
    stack.push("δ", 1.5)

    print(f"Quantum state: {stack.get_quantum_state()}")

    print("\n--- First Collapse ---")
    print(f"Peek (collapses): {stack.peek()}")
    print(f"Collapsed state: {stack.get_collapsed_state()}")

    print("\n--- Popping elements ---")
    while not stack.is_empty():
        print(f"Pop: {stack.pop()}")

    print(f"\nStack is now empty: {stack.is_empty()}")
