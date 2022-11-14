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
