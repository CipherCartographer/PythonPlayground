/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {

    Stack<NestedInteger> nestedStack = new Stack<NestedInteger>();
    public NestedIterator(List<NestedInteger> nestedList) {
        Collections.reverse(nestedList);
        nestedStack.addAll(nestedList);   
    }

    @Override
    public Integer next() {
        return nestedStack.pop().getInteger();
    }

    @Override
    public boolean hasNext() {
        while (!nestedStack.isEmpty()) {
           NestedInteger top = nestedStack.peek();
            if (top.isInteger())
                return true;
           List<NestedInteger> nestedList = nestedStack.pop().getList();
           Collections.reverse(nestedList);
           nestedStack.addAll(nestedList);
        }
        return false;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */