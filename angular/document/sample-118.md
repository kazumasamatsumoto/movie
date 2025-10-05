# #118 「Input/Output のパフォーマンス考慮」

## 概要
Angular v20におけるInput/Outputのパフォーマンス最適化手法。OnPushチェンジ検出戦略とSignalを活用して、不要な再レンダリングを防ぎ、大規模アプリケーションでも滑らかな動作を実現する。

## 学習目標
- OnPushチェンジ検出戦略の効果を理解する
- Signal による効率的な変更検出を学ぶ
- パフォーマンス最適化の実装方法を把握する

## 技術ポイント
- OnPush チェンジ検出戦略
- Signal による変更検出の最適化
- オブジェクト参照の最適化
- 不要な再レンダリングの回避

## 📺 画面表示用コード

### OnPush 戦略の実装
```typescript
@Component({
  selector: 'app-optimized-list',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div *ngFor="let item of items; trackBy: trackByFn">
      {{ item.name }}
    </div>
  `
})
export class OptimizedListComponent {
  @Input() items: Item[] = [];

  trackByFn(index: number, item: Item): number {
    return item.id;
  }
}
```

### Signal を使った最適化
```typescript
@Component({
  selector: 'app-signal-component',
  template: `
    <div *ngIf="user()">
      {{ user()?.name }}
    </div>
    <div>Count: {{ count() }}</div>
    <button (click)="increment()">Increment</button>
  `
})
export class SignalComponent {
  user = input<User>();
  private _count = signal(0);
  count = this._count.asReadonly();

  increment() {
    this._count.update(c => c + 1);
  }
}
```

### 親コンポーネントでの最適化
```typescript
@Component({
  template: `
    <app-signal-component 
      [user]="currentUser"
      (countChange)="onCountChange($event)">
    </app-signal-component>
  `
})
export class ParentComponent {
  currentUser = { id: 1, name: 'John' };

  onCountChange(count: number) {
    // 必要に応じて処理
  }
}
```

## 実践的な活用例
- 大量のデータを扱うリスト表示
- リアルタイム更新が必要なダッシュボード
- インタラクティブなフォーム

## ベストプラクティス
- 適切なチェンジ検出戦略を選択する
- trackBy 関数を使用してリストの最適化を行う
- オブジェクト参照の変更を最小限に抑える
- Signal を活用した効率的な状態管理

## 注意点
- OnPush 戦略使用時は手動での変更検出が必要な場合がある
- 大量のデータを@Input()で渡す場合はパフォーマンスを考慮する
- メモリリークを防ぐため、適切なクリーンアップを行う

## 関連技術
- チェンジ検出戦略
- Signal
- パフォーマンス最適化
- リストレンダリング最適化
