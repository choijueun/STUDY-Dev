### 프로토콜

네트워크에서 데이터를 주고받기 위해 **네트워크를 구성하는 컴퓨터와 네트워크 장비들이 지켜야 할 규칙**

> 사양

프로토콜이 규정한 구체적인 내용

- 누구에게(Who): 전송 상대

- 무엇을(What): 데이터 형식

- 언제(When): 순서와 절차

- 어떻게(How): 전송 방법

> 종류

데이터 전송 목적, 즉 **서비스 종류**에 따라 프로토콜 조합하여 사용

TCP, UDP, IP, HTTP …


## 네트워크 아키텍처

복잡한 네트워크 시스템을 프로토콜의 조합으로 단순화한 것

데이터를 전송하는 과정을 논리적인 단계로 분할하여 각 단계마다 핵심적 기능을 **모둘화**하고 분할된 모듈을 계층적 구조로 배열하는 **계층화**를 통해 네트워크를 추상화시킨 것

### 추상화 Abstraction

복잡한 시스템을 쉽게 이해할 수 있도록 핵심적인 개념(기능)을 뽑아 단순화시키는 방법

### 모듈화와 계층화

> 모듈화

복잡한 시스템을 기능에 따라 **모듈**이라는 작은 단위로 분할하여 설계하는 것

- 핵심은 분할보다는 **연결**

- 모듈을 연결할 수 있는 표준화된 인터페이스가 있어야 함

> 계층화

모듈 간에 시간적 개념을 부여하여 모듈을 일정한 순서로 배열한 것

### 프로토콜과 네트워크 아키텍처

> 프로토콜

네트워크 아키텍처에서 각 계층의 고유한 기능을 정의해 놓은 것

- 각 계층은 기능마다 고유한 프로토콜이 존재

> 네트워크 아키텍처

프로토콜들의 집합

- 각 계층은 프로토콜에 정의된 기능을 수행하면서 제 역할을 한다.

현실에서는 이 설계도에 따라 제작된 커퓨터와 네트워크 장비의 하드웨어 or 소프트웨어가 각 계층의 기능을 구현(implement)

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FMWf4b%2FbtqMcuU7tqE%2Fh9aq0anMBbLcH4tetWl8Q1%2Fimg.png)

### 장점

- 독립성

- 인터페이스를 통한 네트워크 장비 기술 간의 상호 연결성


## OSI 모델과 TCP/IP 모델

> OSI : Open System Interconnection

- 데이터 전송 과정을 7개 계층으로 분류

- 네트워크 통신과정을 개념적으로 설명하는 용도로 활용

- 다른 모델에 영향을 주어 OSI 참조 모델이라고도 불림

> TCP/IP 모델

- 데이터 전송 과정을 4개 계층으로 단순화

- 사실상 표준(De Facto Standard)

### TCP/IP가 사실상 표준이 된 이유

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcnMZww%2FbtqJXU99OPe%2Foym0HqaPNQHAW94LgDOShK%2Fimg.png)

프로토콜을 정하는 것 자체보다 **실제 네트워크에서 동작하는 프로토콜을 구현하는 것을 중시**한 모델

### 데이터 송수신 과정

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fxo5CB%2FbtqMfis8QVh%2FI8y20795Hx96oYqCOKKSjK%2Fimg.png)

> 데이터 송신 컴퓨터

제4계층부터 순서대로 각 계층의 역할 수행

> 데이터 수신 컴퓨터

제1계층부터 순서대로 각 계층의 역할 수행
