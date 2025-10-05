# #126 「Component 通信のデザインパターン」

## 概要
Angular v20におけるコンポーネント通信のデザインパターン。Observer、Publisher-Subscriber、Mediatorパターンなどを適用し、拡張性と保守性の高いアプリケーションアーキテクチャを構築する方法を学ぶ。

## 学習目標
- コンポーネント通信の主要なデザインパターンを理解する
- パターンの適用場面を学ぶ
- 拡張性と保守性の向上を把握する

## 技術ポイント
- Observer パターンの実装
- Publisher-Subscriber パターンの活用
- Mediator パターンの適用
- パターンの組み合わせ

## 📺 画面表示用コード

### Observer パターン
```typescript
@Injectable()
export class DataObserver {
  private observers: ((data: any) => void)[] = [];
  
  subscribe(observer: (data: any) => void) {
    this.observers.push(observer);
  }
  
  notify(data: any) {
    this.observers.forEach(observer => observer(data));
  }
}

@Component({
  selector: 'app-publisher',
  template: `<button (click)="publish()">発行</button>`
})
export class PublisherComponent {
  constructor(private dataObserver: DataObserver) {}
  
  publish() {
    this.dataObserver.notify('New Data');
  }
}
```

### Mediator パターン
```typescript
@Injectable()
export class CommunicationMediator {
  private components = new Map<string, Component>();
  
  register(name: string, component: Component) {
    this.components.set(name, component);
  }
  
  sendMessage(from: string, to: string, message: any) {
    const targetComponent = this.components.get(to);
    if (targetComponent) {
      targetComponent.receiveMessage(message);
    }
  }
}

@Component({
  selector: 'app-mediator-component',
  template: `<div>{{ message }}</div>`
})
export class MediatorComponent implements OnInit {
  message = '';
  
  constructor(private mediator: CommunicationMediator) {}
  
  ngOnInit() {
    this.mediator.register('component1', this);
  }
  
  receiveMessage(message: any) {
    this.message = message;
  }
}
```

## 実践的な活用例
- 複雑な状態管理
- 多対多の通信
- プラグインアーキテクチャ

## ベストプラクティス
- 適切なパターンを選択する
- パターンの組み合わせを検討する
- 過度な抽象化を避ける
- チームでの理解を深める

## 注意点
- パターンの適用コストを考慮する
- 過度な設計を避ける
- 実装の複雑さを管理する

## 関連技術
- デザインパターン
- アーキテクチャ設計
- ソフトウェア設計原則
- 拡張性設計
