### Task 206: Revrese Linked List
First approach - iterative <br>
General idea:<br>
Init: None  1->2->3->4 <br>
1:    None<-1  2->3->4 <br>
2:    None<-1<-2  3->4 <br>
3:    None<-1<-2<-3  4 <br>
4:    None<-1<-2<-3<-4 <br>

By default next elemnt for last (4) is None

Second approach - recursive
General idea:<br>
Start from end of original order and change link step-by-step until None.

### Task 21: Merge two sorted lists
Step-by-step connect tails of two sorted links.
Update node of new linked list on every step, add tail of bigger list at the end.
Input <br>
List1: 1->2 <br>
List2: 1->3->4->5 <br>
        
Initialization step <br>        
List1: 1->2 <br>
List2: 1->3->4->5 <br>
Result: 0 <br>

Step1 <br>
List1: 1->2 <br>
List2: 3->4->5 <br>
Result: 0->1->3->4->5 <br>

Step2 <br>
List1: 2 <br>
List2: 3->4->5 <br>
Result: 0->1->1->2 <br>

Step3 <br>
List2: None <br>
List2: 3->4->5 <br>
Result: 0->1->1->2 <br>
        
Final step (add tail) <br>
List2: None <br>
List2: 3->4->5 <br>
Result: 0->1->1->2->3->4->5 <br>
