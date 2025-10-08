# #247 「CDK Portal の実装」

## 概要
Angular CDK Portal APIを実装レベルで利用し、ComponentPortal・TemplatePortal・PortalOutletを使った動的表示システムを構築します。Portalsを利用したオーバーレイやドッキングUIの例を学びます。

## 学習目標
- PortalModuleのセットアップと主要クラス（ComponentPortal, TemplatePortal, DomPortalOutlet）を理解する
- ComponentPortalをOverlayや任意要素へアタッチする方法を習得する
- PortalOutlet解除や複数ポータル切り替えを実装する

## 技術ポイント
- **PortalModule**: `import { PortalModule } from '@angular/cdk/portal';`
- **ComponentPortal**: コンポーネントをPortal化し、Outletへattach
- **PortalOutlet**: DOM要素やOverlayコンテナをPortalの表示先として利用

# # code?***
