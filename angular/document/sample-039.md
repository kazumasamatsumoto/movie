# #039 「[style] スタイルバインディング」

## 概要
スタイルバインディングは、要素のインラインCSSスタイルを動的に設定する手法です。`[style.property]`構文で個別のスタイルプロパティを制御でき、単位付きの値やオブジェクト形式での複数スタイル設定が可能です。

## 学習目標
- スタイルバインディングの基本構文を理解する
- 単位付きスタイルの設定方法を学ぶ
- 動的なスタイリングの実装方法を習得する

## 技術ポイント
- `[style.property]`による個別スタイル制御
- 単位指定（px、%、emなど）
- オブジェクト形式による複数スタイル設定
- 条件式によるスタイル変更

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class StyleComponent {
  textColor = 'red';
  fontSize = 16;
}
```

```html
<!-- スタイルバインディング -->
<p [style.color]="textColor">テキスト</p>
<div [style.font-size.px]="fontSize">サイズ</div>
```

```html
<!-- 複数スタイル -->
<div [style]="{color: 'blue', fontSize: '20px'}">
```

## 💻 詳細実装例（学習用）

```typescript
// style-binding.component.ts
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-style-binding',
  standalone: true,
  template: `
    <div class="demo">
      <h2>スタイルバインディングの例</h2>

      <!-- 基本的なスタイルバインディング -->
      <section>
        <h3>色の変更</h3>
        <p [style.color]="textColor()">
          このテキストの色は動的に変更されます
        </p>
        <button (click)="changeColor('red')">赤</button>
        <button (click)="changeColor('blue')">青</button>
        <button (click)="changeColor('green')">緑</button>
      </section>

      <!-- 単位付きスタイル -->
      <section>
        <h3>サイズの変更（単位付き）</h3>
        <div [style.width.px]="boxWidth()"
             [style.height.px]="boxHeight()"
             [style.background-color]="bgColor()">
          {{boxWidth()}}px × {{boxHeight()}}px
        </div>
        <button (click)="increaseSize()">拡大</button>
        <button (click)="decreaseSize()">縮小</button>
      </section>

      <!-- フォントサイズ -->
      <section>
        <h3>フォントサイズ</h3>
        <p [style.font-size.px]="fontSize()">
          フォントサイズ: {{fontSize()}}px
        </p>
        <input type="range" min="12" max="48"
               [value]="fontSize()"
               (input)="updateFontSize($event)">
      </section>

      <!-- 複数スタイル（オブジェクト） -->
      <section>
        <h3>複数スタイル（オブジェクト）</h3>
        <div [style]="styleObject()">
          複数のスタイルを一度に適用
        </div>
      </section>

      <!-- 条件付きスタイル -->
      <section>
        <h3>条件付きスタイル</h3>
        <div
          [style.background-color]="temperature() > 30 ? 'red' : 'blue'"
          [style.color]="'white'"
          [style.padding.px]="20">
          温度: {{temperature()}}°C
        </div>
        <button (click)="changeTemperature(35)">暑い</button>
        <button (click)="changeTemperature(15)">寒い</button>
      </section>

      <!-- アニメーション的な使用 -->
      <section>
        <h3>動的な位置とサイズ</h3>
        <div
          [style.transform]="'translateX(' + position() + 'px)'"
          [style.transition]="'all 0.3s ease'"
          class="movable-box">
          移動する要素
        </div>
        <button (click)="moveBox(0)">左</button>
        <button (click)="moveBox(100)">中央</button>
        <button (click)="moveBox(200)">右</button>
      </section>

      <!-- パーセンテージ単位 -->
      <section>
        <h3>プログレスバー</h3>
        <div class="progress-container">
          <div
            [style.width.%]="progress()"
            [style.background-color]="getProgressColor()"
            class="progress-bar">
            {{progress()}}%
          </div>
        </div>
        <button (click)="updateProgress(25)">25%</button>
        <button (click)="updateProgress(50)">50%</button>
        <button (click)="updateProgress(75)">75%</button>
        <button (click)="updateProgress(100)">100%</button>
      </section>

      <!-- グリッドレイアウト -->
      <section>
        <h3>動的グリッド</h3>
        <div [style.display]="'grid'"
             [style.grid-template-columns]="'repeat(' + columns() + ', 1fr)'"
             [style.gap.px]="10"
             class="grid-container">
          @for (item of gridItems; track item) {
            <div class="grid-item">{{item}}</div>
          }
        </div>
        <button (click)="changeColumns(2)">2列</button>
        <button (click)="changeColumns(3)">3列</button>
        <button (click)="changeColumns(4)">4列</button>
      </section>
    </div>
  `,
  styles: [`
    .demo {
      padding: 20px;
    }
    section {
      margin: 30px 0;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    h3 {
      margin-top: 0;
    }
    button {
      margin: 5px;
      padding: 8px 16px;
    }
    .movable-box {
      width: 100px;
      height: 100px;
      background-color: #007bff;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .progress-container {
      width: 100%;
      height: 30px;
      background-color: #f0f0f0;
      border-radius: 4px;
      overflow: hidden;
    }
    .progress-bar {
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: bold;
      transition: width 0.3s ease;
    }
    .grid-container {
      margin: 10px 0;
    }
    .grid-item {
      padding: 20px;
      background-color: #e9ecef;
      border-radius: 4px;
      text-align: center;
    }
  `]
})
export class StyleBindingComponent {
  // 基本スタイル
  textColor = signal('black');
  bgColor = signal('#e9ecef');

  // サイズ
  boxWidth = signal(200);
  boxHeight = signal(100);
  fontSize = signal(16);

  // 複数スタイル
  styleObject = signal({
    'background-color': '#007bff',
    'color': 'white',
    'padding': '20px',
    'border-radius': '8px'
  });

  // 条件付きスタイル
  temperature = signal(25);

  // アニメーション
  position = signal(0);

  // プログレス
  progress = signal(50);

  // グリッド
  columns = signal(3);
  gridItems = Array.from({ length: 12 }, (_, i) => i + 1);

  changeColor(color: string) {
    this.textColor.set(color);
  }

  increaseSize() {
    this.boxWidth.update(v => v + 20);
    this.boxHeight.update(v => v + 10);
  }

  decreaseSize() {
    this.boxWidth.update(v => Math.max(100, v - 20));
    this.boxHeight.update(v => Math.max(50, v - 10));
  }

  updateFontSize(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.fontSize.set(Number(value));
  }

  changeTemperature(temp: number) {
    this.temperature.set(temp);
  }

  moveBox(pos: number) {
    this.position.set(pos);
  }

  updateProgress(value: number) {
    this.progress.set(value);
  }

  getProgressColor(): string {
    const p = this.progress();
    if (p < 30) return '#dc3545';
    if (p < 70) return '#ffc107';
    return '#28a745';
  }

  changeColumns(cols: number) {
    this.columns.set(cols);
  }
}
```

### スタイルバインディングの使い分け

```typescript
@Component({
  template: `
    <!-- ✅ 単一スタイル: [style.property] -->
    <div [style.color]="textColor">シンプル</div>

    <!-- ✅ 単位付き: [style.property.unit] -->
    <div [style.width.px]="width">幅指定</div>
    <div [style.margin.rem]="margin">マージン</div>

    <!-- ✅ 複数スタイル: [style] オブジェクト -->
    <div [style]="{color: 'red', fontSize: '20px'}">複数</div>

    <!-- ✅ 条件付き -->
    <div [style.background-color]="isActive ? 'blue' : 'gray'">条件</div>

    <!-- ❌ 非推奨: ngStyleとの併用 -->
    <div [style.color]="color" [ngStyle]="styles">混在は避ける</div>
  `
})
export class StyleExamplesComponent {}
```

## ベストプラクティス
- 個別のスタイルには`[style.property]`を使用
- 複雑なスタイリングはCSSクラスで管理する
- 単位は明示的に指定する（.px、.%、.emなど）
- アニメーションにはtransitionプロパティを活用する
- 頻繁に変更されるスタイルのみバインディングを使用する

## 注意点
- インラインスタイルはCSSの詳細度が高く、上書きされにくい
- パフォーマンスを考慮し、過度な使用は避ける
- CSSクラスによるスタイリングを優先し、動的な値のみバインディングを使う
- ブラウザのベンダープレフィックスが必要な場合がある

## 関連技術
- [class]バインディング
- ngStyle ディレクティブ
- CSS変数（カスタムプロパティ）
- Renderer2（プログラマティックなスタイル操作）
