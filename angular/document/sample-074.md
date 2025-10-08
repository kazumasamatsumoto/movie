# #074 「Lifecycle の実行順序」

## 概要
Angularコンポーネントで呼び出されるLifecycle Hooksの実行順序を整理し、各フックの位置づけを理解します。

## 学習目標
- 主要フックの発火順序を暗記する
- 初期化系とチェック系のペア関係を把握する
- 順序を意識した設計で副作用の競合を避ける

## 技術ポイント
- **初期段階**: `ngOnChanges` → `ngOnInit` → `ngDoCheck`
- **コンテンツ段階**: `ngAfterContentInit` → `ngAfterContentChecked`
- **ビュー段階**: `ngAfterViewInit` → `ngAfterViewChecked` → （変更検知ごとに`DoCheck`, `AfterContentChecked`, `AfterViewChecked`）
- **終了**: `ngOnDestroy`

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnChanges() { console.log('OnChanges'); }
```

```typescript
ngAfterViewInit() { console.log('AfterViewInit'); }
```

```typescript
ngOnDestroy() { console.log('OnDestroy'); }
```

## 💻 詳細実装例（学習用）
```typescript
import {
  AfterContentChecked,
  AfterContentInit,
  AfterViewChecked,
  AfterViewInit,
  Component,
  DoCheck,
  OnChanges,
  OnDestroy,
  OnInit,
  SimpleChanges,
} from '@angular/core';

@Component({
  selector: 'app-lifecycle-log',
  standalone: true,
  templateUrl: './lifecycle-log.component.html',
})
export class LifecycleLogComponent
  implements
    OnChanges,
    OnInit,
    DoCheck,
    AfterContentInit,
    AfterContentChecked,
    AfterViewInit,
    AfterViewChecked,
    OnDestroy
{
  logs: string[] = [];

  ngOnChanges(_: SimpleChanges): void {
    this.logs.push('OnChanges');
  }
  ngOnInit(): void {
    this.logs.push('OnInit');
  }
  ngDoCheck(): void {
    this.logs.push('DoCheck');
  }
  ngAfterContentInit(): void {
    this.logs.push('AfterContentInit');
  }
  ngAfterContentChecked(): void {
    this.logs.push('AfterContentChecked');
  }
  ngAfterViewInit(): void {
    this.logs.push('AfterViewInit');
  }
  ngAfterViewChecked(): void {
    this.logs.push('AfterViewChecked');
  }
  ngOnDestroy(): void {
    console.log('OnDestroy');
  }
}
```

```html
<ol>
  <li @for (log of logs; track log)>{{ log }}</li>
</ol>
```

## ベストプラクティス
- 初期化とチェックで重複処理を避けるため、フックごとの目的をコメントや関数名で明示する
- 実行順序をテストで確認したい場合はspyOnを利用する
- DevToolsや`console.table`を使って順序を可視化すると理解が定着する

## 注意点
- `ngOnChanges`はInputがある場合のみ、`ngAfterContent*`は内容投影がある場合に意味を持つ
- `ngAfterViewChecked`は変更検知のたびに呼ばれるためログが膨大になる
- `ngOnDestroy`はルートコンポーネントには呼ばれない（アプリ終了時はブラウザがプロセスを破棄）

## 関連技術
- Angular DevTools Profiler
- ChangeDetectionStrategy.OnPushとの関係
- コンポーネント再作成時のライフサイクル挙動
