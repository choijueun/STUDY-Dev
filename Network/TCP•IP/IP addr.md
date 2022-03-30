출처: ****[IP 주소 의미와 체계 및 서브넷 마스크](https://better-together.tistory.com/118?category=887984)****
<br/>

## IP 주소

인터넷에 접속한 컴퓨터와 라우터는 고유한 IP 주소를 할당받는다.

인터넷 계층의 IP 프로토콜은 IP 주소를 통해 호스트나 네트워크 장비를 식별한다.

모든 컴퓨터나 라우터의 **IP 주소는 유일**해야 한다.

- IPv4
    - Internet Protocol version 4
    - 현재 일반적으로 사용중
- IPv6
    - IPv4보다 많은 수의 IP 주소 할당 가능

<br/>

## IPv4

이진수 32자리로 구성

→ 32bit

Dotted-decimal notation

→ 8비트씩 4그룹으로 나누어 각 그룹을 십진수로 변환, 경계에 ‘.’ 넣음

*ex: 192.168.100.0*

<br/>

### 구성

1. **Network Part**: 호스트가 속한 네트워크 주소
2. **Host Part**: 호스트의 주소
    
    *컴퓨터뿐만이 아니라 IP 주소가 할당되는 라우터를 포함*

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FB82mo%2FbtqNNi76sb9%2FiSw0UPN9LQloCd1lxeNR2k%2Fimg.png)

네트워크나 호스트를 다른 네트워크나 호스트와 구분하는 역할.

서로 다른 네트워크끼리 통신하려면 라우터가 필요하다.

수신지 IP 주소의 네트워크 부를 보고 대상 라우터를 찾아 IP 패킷 전송

<br/>

### IP 주소 클래스

8비트씩 나눈 그룹을 조합하여 네트워크 부와 호스트 부를 정한다.

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fy8x2n%2FbtqNQwYPRvr%2FDZcDOzjEiCd6hwRfJBkHFK%2Fimg.png)

> 클래스 A
> 

앞 8비트를 네트워크 부로, 다음 24비트를 호스트 부로 나눈다.

네트워크 부 첫 비트는 클래스 A 식별 비트인 ‘0’

: 00000000-011111111 (이진수) = 0-127 (십진수)

> 클래스 B
> 

앞 16비트를 네트워크 부로, 다음 16비트를 호스트 부로 나눈다.

네트워크 부 맨 앞 2비트는 클래스 B 식별 비트인 ‘10’

: 10000000-10111111 (이진수) = 128-191

> 클래스 C
> 

앞 24비트를 네트워크 부로, 다음 8비트를 호스트 부로 나눈다.

네트워크 부 맨 앞 3비트는 클래스 C의 식별 비트인 ‘110’

: 11000000-11011111 (이진수) = 192-223

<br/>

### 특수 목적 IP 주소

클래스 불문 호스트 부의 모든 비트가 0인 번호는 네트워크 주소, 모든 비트가 1인 번호는 브로드캐스트 주소

1. 네트워크 주소
    - 전체 네트워크에서 작은 네트워크를 식별할 때 사용
    - 호스트 부 십진수로 0이면 그 네트워크를 대표하는 주소
2. 브로드캐스트 주소
    - 하나의 네트워크에 있는 모든 호스트에 동시에 데이터를 보낼 때 사용되는 전용 IP 주소
    - 호스트 부 십진수로 255

<br/>

### 서브넷팅과 서브넷

클래스 A와 클래스 B에서 많은 IP 주소가 낭비된다.

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbLDjgW%2FbtqNU2Cuug8%2F02uFH1sdsBsygX5K8oWUT0%2Fimg.png)

> 서브넷팅
> 

IP 주소를 효율적으로 활용하기 위해 이와 같은 대규모 네트워크를 더 작은 네트워크로 분할하는 것

호스트 부의 비트를 서브넷 부로 변경

> 서브넷
> 

분할된 네트워크

서브넷팅(논리적인 방법)으로 분할된 서브넷은 물리적인 방법(라우터)으로 구별된다.

서로 통신하기 위해서는 라우터 필요

<br/>

### 서브넷 마스크
- IP 주소의 네트워크 부와 호스트 부의 경계를 식별하기 위해 만든 **식별자**.
- 1비트 단위로 네트워크 부를 구성할 수 있어 네트워크 세분화
- 반드시 **연속**된 ‘1’과 **연속**된 ‘0’으로 구성. 0과 1이 교대로 나타나지 않음.

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdhZD1c%2FbtqNQbm9E11%2Fi3A3mZj3px0rYm1DedeAj0%2Fimg.png)

- 서브넷 마스크 비트 1: IP 주소 네트워크 부
- 서브넷 마스크 비트 0: IP 주소 호스트 부

![Untitled](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbh762H%2FbtqNRI5EK9R%2FKCrxAYpRDFkLphQmZtCRHK%2Fimg.png)

