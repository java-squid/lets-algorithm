## Sort
### Bubble sort
- 첫 인덱스부터 순회하며 앞, 뒤 대소 관계를 비교하는 정렬 방식
- 구현은 간단하지만 O(n^2)의 시간복잡도를 가진다.
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/bubblesort/BubbleSort.java

### Selection sort
- 버블정렬과 마찬가지로 O(n^2)의 성능을 가진다.
- 구현방법
  - 배열을 순회하면서 최소(혹은 최대)값을 특정 변수에 누적한다. 
  - 순회가 끝났을 때 해당 변수에 저장된 값이 최소(혹은 최대) 값이고, 이 값을 정렬되지 않은 영역의 맨 앞 인덱스에 위치시킨다. 
    이를 (배열의 길이 - 1)까지 반복한다.
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/selectionsort/SelectionSort.java

### Insertion sort
- 정렬되지 않은 구간 (두 번째 인덱스부터 끝 인덱스) 요소를 순회하며 정렬된 구간(첫 인덱스 요소 하나로 시작하여 삽입이 한번 수행될 때 마다 점차 늘어감)의 특정 인덱스에 해당 요소를 삽입하여 정렬 구간을 넓혀 나가는 방식
    - 정렬된 구간의 시작지점 = index 0
    - 정렬되지 않은 구간의 시작지점 = 정렬된 구간의 끝지점 + 1
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/insertionsort/InsertionSort.java

### Quick sort
- 분할 정복 알고리즘
- pivot을 지정하고 지정 된 pivot과의 대소를 기준으로 포인터 2개를 이동하며 정렬
- 평균적으로 O(nlogn)의 성능. 드물게 pivot이 한쪽으로 치우치는 경우 O(n^2)
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/quicksort/QuickSort.java

### Merge sort
- 크기가 N인 컬렉션이 있을 때, N만큼 그룹을 나누고 각 그룹을 병합하면서 정렬하는 방법
- 시간 복잡도 : O(nlongn)
- quick sort와 비슷한 시간 복잡도를 갖는 것으로 평가 됨
    - 차이점
        - quick sort : pivot에 따라 최악의 시간 복잡도 n^2까지 나타날 수 있음 (극히 드문 경우)
        - merge sort : nlogn의 고정 된 시간복잡도를 갖게 되지만, 병합 할 배열을 따로 선언해야 하여 quick sort보다 더 많은 메모리 사용
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/mergesort/MergeSort.java


## Python
### Sort
- Python 내부에서는 Tim sort를 사용한다고 한다.
  - https://d2.naver.com/helloworld/0315536

## 다시 볼 문제
- [1517](https://www.acmicpc.net/problem/1517)
  - merge sort 정렬 과정에 버블 정렬이 적용되는 것을 제대로 이해하고 있지 못하였다. 

