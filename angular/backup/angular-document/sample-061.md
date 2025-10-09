# #061 「Lifecycle Hooks とは？コンポーネントの一生」

## 概要
Angularコンポーネントの生成から破棄まで、処理を挟めるタイミングを提供するLifecycle Hooksの全体像を学びます。

## 学習目標
- コンポーネントのライフサイクル段階を説明できる
- 各フックがおおよそどの順序で呼ばれるか理解する
- 適切なタイミングに処理を割り当てる判断基準を身につける

## 技術ポイント
- **Lifecycle Hooks**: `OnInit`, `OnDestroy`, `AfterViewInit`などのインターフェースでタイミングを扱う
- **順序理解**: 生成→初期化→変更検知→ビュー/コンテンツ→破棄の流れ
- **責務分離**: 各フックに役割を限定して副作用を安全に扱う

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
export class LifecycleDemoComponent
  implements OnInit, OnDestroy {}
```

```typescript
ngOnInit(): void {
  console.log('初期化');
}
```

```typescript
ngOnDestroy(): void {
  console.log('破棄');
}
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnInit, OnDestroy, OnChanges, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-lifecycle-demo',
  standalone: true,
  templateUrl: './lifecycle-demo.component.html',
})
export class LifecycleDemoComponent implements OnInit, OnDestroy, OnChanges {
  logs: string[] = [];

  ngOnChanges(changes: SimpleChanges): void {
    this.logs.push(`OnChanges: ${Object.keys(changes).join(', ')}`);
  }

  ngOnInit(): void {
    this.logs.push('OnInit: 初期化処理');
  }

  ngOnDestroy(): void {
    console.log('OnDestroy: 破棄前の後始末');
  }
}
```

```html
<h3>Lifecycle Logs</h3>
<ul>
  <li @for (log of logs; track log)>{{ log }}</li>
</ul>
```

## ベストプラクティス
- フックを実装する際は対になるインターフェースをimplementsし、型ミスを防ぐ
- ログなどのデバッグ目的を除き、重い処理は必要なタイミングだけに限定する
- 頻繁に利用するフック（ngOnInit/ngOnDestroy）に責務を集中させる

## 注意点
- constructorはライフサイクルに含まれずDI専用と考える
- 破棄時ログは必ずしも画面に出ないため、必要ならサービスへ委譲する
- フックは生成ごとに呼ばれるので、再利用時にも実行される点を理解する

## 関連技術
- Standalone Component設計
- Angular DevToolsでのLifecycle可視化
- SignalsとLifecycleの統合
