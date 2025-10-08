# #083 「Lifecycle でのリソース解放」

## 概要
外部API接続やブラウザリソース（WebSocket、IndexedDB、オーディオなど）をLifecycle Hooksで適切に解放し、アプリの安定性を保つ方法を学びます。

## 学習目標
- リソース獲得と解放のペアをLifecycleで管理する
- `ngOnDestroy`でリソースを確実に解放するコードを書く
- サービス層の`dispose`パターンを導入する

## 技術ポイント
- **取得**: `ngOnInit`/`ngAfterViewInit`で接続やリソースの初期化
- **解放**: `ngOnDestroy`で`close`, `abort`, `disconnect`を呼ぶ
- **サービス連携**: コンポーネントはサービスの`dispose()`を呼び、実装詳細をカプセル化

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
private mediaStream?: MediaStream;
```

```typescript
ngAfterViewInit() {
  this.mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
}
```

```typescript
ngOnDestroy() {
  this.mediaStream?.getTracks().forEach((track) => track.stop());
}
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnDestroy, OnInit } from '@angular/core';

class SocketService {
  private socket?: WebSocket;

  connect(url: string): void {
    this.socket = new WebSocket(url);
  }

  dispose(): void {
    this.socket?.close();
  }
}

@Component({
  selector: 'app-resource-manager',
  standalone: true,
  templateUrl: './resource-manager.component.html',
  providers: [SocketService],
})
export class ResourceManagerComponent implements OnInit, OnDestroy {
  mediaStream?: MediaStream;

  constructor(private readonly socketService: SocketService) {}

  async ngOnInit(): Promise<void> {
    this.socketService.connect('wss://example.com');
    this.mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
  }

  ngOnDestroy(): void {
    this.mediaStream?.getTracks().forEach((track) => track.stop());
    this.socketService.dispose();
  }
}
```

```html
<p>マイク入力を取得し、破棄時に停止します。</p>
```

## ベストプラクティス
- リソース操作をサービスに集約し、Lifecycleではサービスの`connect`/`dispose`を呼ぶだけにする
- `AbortController`を使ってfetchやStreamを中断できるようにする
- `try/finally`で接続失敗時にも後始末が走るようにする

## 注意点
- ブラウザ権限が必要なAPI（カメラ、マイク）はエラーハンドリングを行う
- `WebSocket.close()`には終了コードを渡して状態を明確にする
- SSR環境ではブラウザAPIが使えないため、プラットフォーム判定を入れる

## 関連技術
- `AbortController`と`signal`
- Angular Serviceパターン (`ngOnDestroy`のあるサービス)
- Web API（WebSocket, MediaDevices, BroadcastChannel）
