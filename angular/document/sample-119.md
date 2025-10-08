# #119 「Input/Output のデバッグ方法」

## 概要
@Input() / @Output()でデータやイベントが期待通りに流れているかを確認するためのデバッグ手法を紹介します。

## 学習目標
- Angular DevToolsやブラウザコンソールで状態を確認する方法を理解する
- テンプレート内で一時的に値を可視化する手段を学ぶ
- EventEmitterやSignalsでログを挿入するポイントを把握する

## 技術ポイント
- **Angular DevTools**: Componentsタブで@Input()の値と@Outputイベントの履歴を確認
- **テンプレートログ**: `{{ value | json }}`や`@if (debug()) { ... }`
- **RxJS tap**: EventEmitterをObservableとして`pipe(tap())`しログ出力

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<pre class="debug">{{ inputValue | json }}</pre>
```

```typescript
this.saved.pipe(tap(console.log)).subscribe();
```

```html
@if (debugMode) { <p>DEBUG: {{ status }}</p> }
```

## 💻 詳細実装例（学習用）
```typescript
// debug-demo.component.ts
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-debug-demo',
  standalone: true,
  templateUrl: './debug-demo.component.html',
  styleUrls: ['./debug-demo.component.css'],
})
export class DebugDemoComponent {
  @Input() debug = false;

  private _status = 'pending';

  @Input()
  set status(value: string) {
    this._status = value;
    if (this.debug) {
      console.log('[Input status]', value);
    }
  }
  get status(): string {
    return this._status;
  }

  @Output() saved = new EventEmitter<string>();

  constructor() {
    this.saved.pipe(tap((value) => console.log('[Output saved]', value))).subscribe();
  }

  save(): void {
    this.saved.emit(`status: ${this.status}`);
  }
}
```

```html
<!-- debug-demo.component.html -->
<button type="button" (click)="save()">保存</button>
@if (debug) {
  <pre class="debug">status: {{ status }}</pre>
}
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { DebugDemoComponent } from './debug-demo.component';

@Component({
  selector: 'app-debug-page',
  standalone: true,
  imports: [DebugDemoComponent],
  template: `
    <app-debug-demo
      [status]="status"
      [debug]="true"
      (saved)="handleSaved($event)"
    ></app-debug-demo>
  `,
})
export class DebugPageComponent {
  status = 'pending';

  handleSaved(result: string): void {
    console.log('親で受信:', result);
  }
}
```

## ベストブラクティス
- Angular DevToolsで@Input()や@Output()の値を確認し、どのタイミングで変わるかを追う
- 一時的にテンプレートへ`{{ value | json }}`を表示する場合、`debug`プロパティで制御して本番で無効化する
- EventEmitterやObservableに`tap`を挿入して、ハンドラ実行前にログを出す

## 注意点
- ログの出しすぎはパフォーマンス低下につながるので、デバッグ時のみ有効化する
- console.logはブラウザのDevToolsに依存するため、CIやサーバーログには出ない
- テンプレートのdebug用出力を本番に残さないようにする（スタイルで非表示にするのではなく削除する）

## 関連技術
- Angular DevTools Components/Profiler
- RxJS tap operator
- Angular Logging（NGX Loggerなど） and environment-based logging
