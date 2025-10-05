# #039 「[style] スタイルバインディング」台本

四国めたん「[style] スタイルバインディングについて学びましょう！」
ずんだもん「インラインスタイルを動的に変更できるの？」
四国めたん「はい！プロパティバインディングでCSSスタイルを動的に設定できます」
ずんだもん「どんな場面で使うの？」
四国めたん「動的な色変更、サイズ調整、位置制御などです」
ずんだもん「ngStyleディレクティブもある？」
四国めたん「ngStyleを使うとより複雑なスタイル制御ができます」

---

## 📺 画面表示用コード

// 基本的なスタイルバインディング
```typescript
@Component({
  selector: 'app-style-basic',
  standalone: true,
  template: `
    <div class="style-demo">
      <h2>基本的なスタイルバインディング</h2>
      <div [style.color]="textColor"
           [style.font-size]="fontSize"
           [style.background-color]="backgroundColor">
        動的なスタイル適用
      </div>
      <button (click)="changeColors()">色変更</button>
      <button (click)="changeSize()">サイズ変更</button>
    </div>
  `,
  styles: [`
    .style-demo {
      padding: 20px;
    }
    div {
      padding: 20px;
      margin: 10px 0;
      border: 2px solid #ccc;
      transition: all 0.3s;
    }
  `]
})
export class StyleBasicComponent {
  textColor = 'blue';
  fontSize = '16px';
  backgroundColor = 'lightgray';
  
  colors = ['blue', 'red', 'green', 'purple'];
  sizes = ['14px', '16px', '18px', '20px'];
  colorIndex = 0;
  sizeIndex = 0;
  
  changeColors() {
    this.colorIndex = (this.colorIndex + 1) % this.colors.length;
    this.textColor = this.colors[this.colorIndex];
    this.backgroundColor = `light${this.colors[this.colorIndex]}`;
  }
  
  changeSize() {
    this.sizeIndex = (this.sizeIndex + 1) % this.sizes.length;
    this.fontSize = this.sizes[this.sizeIndex];
  }
}
```

// 計算されたスタイル値
```typescript
@Component({
  selector: 'app-calculated-style',
  standalone: true,
  template: `
    <div class="calculated-demo">
      <h2>計算されたスタイル値</h2>
      <div [style.width]="width + 'px'"
           [style.height]="height + 'px'"
           [style.margin-left]="margin + 'px'">
        サイズ: {{width}}x{{height}}
      </div>
      <button (click)="resize()">リサイズ</button>
    </div>
  `,
  styles: [`
    .calculated-demo {
      padding: 20px;
    }
    div {
      background-color: #007bff;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.3s;
    }
  `]
})
export class CalculatedStyleComponent {
  width = 100;
  height = 100;
  margin = 0;
  
  resize() {
    this.width += 20;
    this.height += 10;
    this.margin += 5;
  }
}
```

// ngStyleを使った複雑な制御
```typescript
@Component({
  selector: 'app-ngstyle-demo',
  standalone: true,
  imports: [NgStyle],
  template: `
    <div class="ngstyle-demo">
      <h2>ngStyleを使った複雑な制御</h2>
      <div [ngStyle]="getStyles()">
        複数のスタイル制御
      </div>
      <button (click)="toggleTheme()">テーマ切り替え</button>
    </div>
  `,
  styles: [`
    .ngstyle-demo {
      padding: 20px;
    }
    div {
      padding: 20px;
      margin: 10px 0;
      border: 2px solid;
      transition: all 0.3s;
    }
  `]
})
export class NgStyleDemoComponent {
  isDark = false;
  
  getStyles() {
    return {
      'color': this.isDark ? 'white' : 'black',
      'background-color': this.isDark ? '#333' : '#fff',
      'border-color': this.isDark ? '#666' : '#ccc',
      'border-radius': this.isDark ? '10px' : '0px',
      'box-shadow': this.isDark ? '0 4px 8px rgba(0,0,0,0.3)' : 'none'
    };
  }
  
  toggleTheme() {
    this.isDark = !this.isDark;
  }
}
```
